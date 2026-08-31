#!/bin/bash
cd /home/node/openclaw/books/cognition-economy
for n in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16; do
  ch="chapters/ch${n}.md"
  cs="case-studies/ch${n}-case-study.md"
  [ -f "$ch" ] && [ -f "$cs" ] || { echo "MISSING $n"; continue; }
  # header = first 4 lines (title, subtitle, blank, ---) plus blank line
  head -4 "$cs" > .diffwork/newcs_$n.md
  echo "" >> .diffwork/newcs_$n.md
  awk '/^## Case Study/{f=1} f&&/^## /&&!/^## Case Study/{exit} f{print}' "$ch" >> .diffwork/newcs_$n.md
  mv .diffwork/newcs_$n.md "$cs"
  echo "rebuilt $cs ($(wc -l < "$cs") lines)"
done
