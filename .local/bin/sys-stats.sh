#!/usr/bin/env bash

# https://gitlab.com/Zaney/dotfiles/-/blob/main/.local/bin/sys-stats

CPUTemp=$(sensors | grep 'edge:' | awk '{ print substr ($0, 16 ) }')

notify-send -t 8000 "$(
free -m | awk 'NR==2{printf "🐏 Usage: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
top -bn1 | grep load | awk '{printf "🧠 Load: %.2f\n", $(NF-2)}'
printf "🌡️ CPU: $CPUTemp"
)"
