#!/usr/bin/env bash

dir="$HOME/.config/rofi/launchers/type-6"
theme='style-1'

rofi \
    -modi "clipboard:greenclip print" \
    -show clipboard \
    -theme ${dir}/${theme}.rasi
