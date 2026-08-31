#!/bin/bash
cd /home/node/openclaw/books/cognition-economy
mkdir -p .diffwork
for n in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16; do
  ch="chapters/ch${n}.md"
  cs="case-studies/ch${n}-case-study.md"
  [ -f "$ch" ] || continue
  [ -f "$cs" ] || continue
  awk '/^## Case Study/{f=1} f&&/^## /&&!/^## Case Study/{exit} f{print}' "$ch" > .diffwork/chapcase_$n.txt
  awk '/^## Case Study/{f=1} /^### Discussion Guidelines/{exit} f{print}' "$cs" > .diffwork/cscase_$n.txt
  echo "=== ch$n === (chapter: $(wc -l < .diffwork/chapcase_$n.txt) lines, csfile: $(wc -l < .diffwork/cscase_$n.txt) lines)"
  diff .diffwork/chapcase_$n.txt .diffwork/cscase_$n.txt | head -30
done
