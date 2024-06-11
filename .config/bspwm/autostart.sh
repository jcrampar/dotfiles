#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run sxhkd -c ~/.config/bspwm/sxhkd/sxhkdrc &
run polybar &
picom --config $HOME/.config/bspwm/picom/picom.conf &
feh --bg-fill --no-fehbg --randomize ~/Pictures/wallpapers/all/*