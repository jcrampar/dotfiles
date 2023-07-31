#!/usr/bin/env bash

notify-send -t 4500 "$(curl -s 'wttr.in/{Nashville,Memphis}?format=3')"
