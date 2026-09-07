#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESTINATION="${1:-$HOME/.codex/skills/easy-paper}"

mkdir -p "$DESTINATION"
cp "$SOURCE_DIR/SKILL.md" "$DESTINATION/SKILL.md"

for dir in agents assets references scripts docs examples; do
  if [ -d "$SOURCE_DIR/$dir" ]; then
    mkdir -p "$DESTINATION/$dir"
    cp -R "$SOURCE_DIR/$dir/." "$DESTINATION/$dir/"
  fi
done

echo "Easy-Paper installed to $DESTINATION"
echo 'Restart Codex or open a new task, then invoke: $easy-paper'
