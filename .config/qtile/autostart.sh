#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time

run feh --randomize --bg-fill /usr/share/wallpapers/*