#!/usr/bin/env bash

## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
#
## Rofi   : Launcher (Modi Drun, Run, File Browser, Window)
#
## Available Styles
#
## style-1     style-2     style-3     style-4     style-5
## style-6     style-7     style-8     style-9     style-10
## style-11    style-12    style-13    style-14    style-15

# dir="$HOME/.config/rofi/launchers"
# type='type-1'
# theme='style-1'

# command="rofi \
#         -show $1 \
#         -theme ${dir}/${type}/${theme}.rasi"

# ## Run

# case
# eval $command


type=1
style=1
show="drun"
while (( $# > 1 )); do case $1 in
    --show)
        show="$2"
    ;;
    --type)
        type="$2"
    ;;
    --style) 
        style="$2";;
    *) break;
esac; shift 2
done
dir="$HOME/.config/rofi/launchers/type-$type/style-$style.rasi"
command="rofi \
        -show ${show} \
        -theme ${dir}"

eval $command