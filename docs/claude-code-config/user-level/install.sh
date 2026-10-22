#!/usr/bin/env bash
# Install the user-level Claude Code skills and agents in this directory into
# ~/.claude (or $CLAUDE_CONFIG_DIR). Existing files that differ are skipped
# unless --force is given; with --force they are backed up to <file>.bak-<timestamp>
# first. Files removed from this source directory are not removed from the target.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
FORCE=0
if [[ $# -gt 1 ]]; then echo "usage: $0 [--force]" >&2; exit 2; fi
case "${1:-}" in
  --force) FORCE=1 ;;
  "") ;;
  *) echo "usage: $0 [--force]" >&2; exit 2 ;;
esac
STAMP="$(date +%Y%m%d-%H%M%S)"

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
    cp "$target" "$target.bak-$STAMP"
  fi
  mkdir -p "$(dirname "$target")"
  cp "$file" "$target"
  echo "installed: $target"
  installed=$((installed + 1))
done < <(find "$SRC/skills" "$SRC/agents" -type f -print0)

echo "done: $installed installed, $unchanged unchanged, $skipped skipped -> $DEST"
if [[ $skipped -gt 0 ]]; then
  echo "warning: $skipped file(s) differ and were NOT updated; rerun with --force to overwrite" >&2
fi
