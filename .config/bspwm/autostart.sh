#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run sxhkd -c ~/.config/bspwm/sxhkd/sxhkdrc &
run polybar &
