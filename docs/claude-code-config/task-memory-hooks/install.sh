#!/usr/bin/env bash
# Install the task-memory hooks into the user-level Claude Code config.
#
#   ./install.sh [--tmux-autocompact] [--background-checkpoints]
#                [--autocompact-pct N | --no-autocompact-pct]
#
# Idempotent: re-running replaces this bundle's hook entries and leaves every
# other hook, env var and setting alone. settings.json is backed up first.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
DEST="$CLAUDE_DIR/hooks/task-memory"
TM_HOME="$CLAUDE_DIR/task-memory"
TMUX_AUTOCOMPACT=0
MODE=inline
PCT=60

while [ $# -gt 0 ]; do
  case "$1" in
    --tmux-autocompact) TMUX_AUTOCOMPACT=1 ;;
    --background-checkpoints) MODE=background ;;
    --autocompact-pct) PCT="${2:?--autocompact-pct needs a value 1-100}"; shift ;;
    --no-autocompact-pct) PCT="" ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

command -v python3 >/dev/null || { echo "python3 is required" >&2; exit 1; }
if [ -n "$PCT" ] && ! { [ "$PCT" -ge 1 ] 2>/dev/null && [ "$PCT" -le 100 ]; }; then
  echo "--autocompact-pct must be an integer from 1 to 100 (got: $PCT)" >&2; exit 2
fi

# Tested on Claude Code 2.1.307. Older versions may not know the PostCompact
# event or the SessionStart "compact" source; warn rather than guess.
TESTED="2.1.307"
if command -v claude >/dev/null; then
  CC_VERSION="$(claude --version 2>/dev/null | grep -Eo '^[0-9]+\.[0-9]+\.[0-9]+' || true)"
  if [ -n "$CC_VERSION" ] && [ "$(printf '%s\n%s\n' "$TESTED" "$CC_VERSION" | sort -t. -k1,1n -k2,2n -k3,3n | head -1)" != "$TESTED" ]; then
    echo "warning: Claude Code $CC_VERSION is older than $TESTED (the version these hooks were tested on)." >&2
    echo "         If /hooks or settings validation complains, update Claude Code or run ./uninstall.sh." >&2
  fi
fi

mkdir -p "$DEST" "$TM_HOME"
cp "$SRC/hooks/task_memory.py" "$DEST/task_memory.py"
chmod +x "$DEST/task_memory.py"
[ -f "$TM_HOME/config.json" ] || cp "$SRC/config.default.json" "$TM_HOME/config.json"

python3 - "$CLAUDE_DIR" "$DEST" "$TM_HOME" "$TMUX_AUTOCOMPACT" "$PCT" "$MODE" <<'PY'
import json, sys, shutil, time
from pathlib import Path

claude_dir, dest, tm_home, tmux, pct, mode = sys.argv[1:7]
settings_path = Path(claude_dir) / "settings.json"
state_path = Path(tm_home) / "install-state.json"
MARK = "task-memory/task_memory.py"

settings = {}
if settings_path.exists():
    settings = json.loads(settings_path.read_text() or "{}")
    backup = settings_path.with_name(f"settings.json.bak-task-memory-{time.strftime('%Y%m%d-%H%M%S')}")
    shutil.copy2(settings_path, backup)
    print(f"backed up {settings_path} -> {backup}")

hooks = settings.setdefault("hooks", {})
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

script = Path(dest) / "task_memory.py"
for event, matcher, sub, timeout in (
    ("Stop", None, "stop", 20),
    ("PreCompact", None, "pre-compact", 15),
    ("PostCompact", None, "post-compact", 15),
    ("SessionStart", "startup|resume|clear|compact", "session-start", 10),
):
    group = {"hooks": [{"type": "command", "command": f'python3 "{script}" {sub}', "timeout": timeout}]}
    if matcher:
        group = {"matcher": matcher, **group}
    hooks.setdefault(event, []).append(group)

state = json.loads(state_path.read_text()) if state_path.exists() else {}
env = settings.setdefault("env", {})
if pct:
    current = env.get("CLAUDE_AUTOCOMPACT_PCT_OVERRIDE")
    if current is None or (state.get("env_set") and current == state["env_set"]):
        env["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] = pct
        state["env_set"] = pct
    else:
        print(f"kept your existing CLAUDE_AUTOCOMPACT_PCT_OVERRIDE={env['CLAUDE_AUTOCOMPACT_PCT_OVERRIDE']}")
elif state.get("env_set") and env.get("CLAUDE_AUTOCOMPACT_PCT_OVERRIDE") == state["env_set"]:
    del env["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"]
    state.pop("env_set")
if not env:
    del settings["env"]

config_path = Path(tm_home) / "config.json"
config = json.loads(config_path.read_text())
config["tmux_autocompact"] = tmux == "1"
config["checkpoint_mode"] = mode
config_path.write_text(json.dumps(config, indent=2) + "\n")

settings_path.write_text(json.dumps(settings, indent=2) + "\n")
state_path.write_text(json.dumps(state, indent=2) + "\n")
print(f"hooks registered in {settings_path}")
PY

echo "installed task-memory hooks -> $DEST"
echo "data + config        -> $TM_HOME (edit config.json to tune thresholds)"
[ "$TMUX_AUTOCOMPACT" = 1 ] && echo "tmux auto-/compact: ON (only acts when Claude runs inside tmux)"
echo "checkpoint mode: $MODE"
echo "Restart Claude Code (or open /hooks) to load the hooks."
