#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time

#lxsession &

run feh --randomize --bg-fill /usr/share/wallpapers/*
rclone mount GoogleDrive_juanc.rampar: ~/GoogleDrive_juanc.rampar --daemon --cache-dir ~/.cache/rclone --vfs-cache-mode writes
rclone mount OneDrive_Freeway: ~/OneDrive_Freeway --daemon --cache-dir ~/.cache/rclone --vfs-cache-mode writes