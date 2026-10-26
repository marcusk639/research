#!/usr/bin/env bash
# Remove the task-memory hooks from the user-level Claude Code config.
#
#   ./uninstall.sh [--purge]    --purge also deletes saved checkpoints/learnings
#
# Serena and claude-mem memories written by the hooks are left in place.
set -euo pipefail

CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
DEST="$CLAUDE_DIR/hooks/task-memory"
TM_HOME="$CLAUDE_DIR/task-memory"
PURGE=0
[ "${1:-}" = "--purge" ] && PURGE=1

python3 - "$CLAUDE_DIR" "$TM_HOME" <<'PY'
import json, sys, shutil, time
from pathlib import Path

claude_dir, tm_home = sys.argv[1:3]
settings_path = Path(claude_dir) / "settings.json"
state_path = Path(tm_home) / "install-state.json"
MARK = "task-memory/task_memory.py"
if not settings_path.exists():
    sys.exit(0)
settings = json.loads(settings_path.read_text() or "{}")
shutil.copy2(settings_path, settings_path.with_name(f"settings.json.bak-task-memory-{time.strftime('%Y%m%d-%H%M%S')}"))

hooks = settings.get("hooks", {})
for event in list(hooks):
    groups = []
    for group in hooks[event]:
        kept = [h for h in group.get("hooks", []) if MARK not in h.get("command", "")]
        if kept:
            groups.append({**group, "hooks": kept})
    if groups:
        hooks[event] = groups
    else:
        del hooks[event]
if "hooks" in settings and not hooks:
    del settings["hooks"]

state = json.loads(state_path.read_text()) if state_path.exists() else {}
env = settings.get("env", {})
if state.get("env_set") and env.get("CLAUDE_AUTOCOMPACT_PCT_OVERRIDE") == state["env_set"]:
    del env["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"]
    if not env:
        del settings["env"]
    state.pop("env_set")
    if state_path.exists():
        state_path.write_text(json.dumps(state, indent=2) + "\n")

settings_path.write_text(json.dumps(settings, indent=2) + "\n")
print(f"hooks removed from {settings_path}")
PY

rm -rf "$DEST"
if [ "$PURGE" = 1 ]; then
  rm -rf "$TM_HOME"
  echo "purged $TM_HOME"
else
  echo "kept saved checkpoints in $TM_HOME (use --purge to delete)"
fi
