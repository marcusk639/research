#!/usr/bin/env bash
# Install the user-level Claude Code skills and agents in this directory into
# ~/.claude (or $CLAUDE_CONFIG_DIR). Existing files that differ are skipped
# unless --force is given; with --force they are backed up to <file>.bak first.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
FORCE=0
case "${1:-}" in
  --force) FORCE=1 ;;
  "") ;;
  *) echo "usage: $0 [--force]" >&2; exit 2 ;;
esac

installed=0; skipped=0; unchanged=0
while IFS= read -r -d '' file; do
  rel="${file#"$SRC"/}"
  target="$DEST/$rel"
  if [[ -e "$target" ]]; then
    if cmp -s "$file" "$target"; then
      unchanged=$((unchanged + 1)); continue
    fi
    if [[ $FORCE -eq 0 ]]; then
      echo "skip (differs; rerun with --force): $target"
      skipped=$((skipped + 1)); continue
    fi
    cp "$target" "$target.bak"
  fi
  mkdir -p "$(dirname "$target")"
  cp "$file" "$target"
  echo "installed: $target"
  installed=$((installed + 1))
done < <(find "$SRC/skills" "$SRC/agents" -type f -print0)

echo "done: $installed installed, $unchanged unchanged, $skipped skipped -> $DEST"
