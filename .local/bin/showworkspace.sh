#!/usr/bin/env bash

Deskname=$(bspc query -D -d focused --names)
dunstify -a "showworkspace" -u low -r 9994 "Workspace $Deskname"