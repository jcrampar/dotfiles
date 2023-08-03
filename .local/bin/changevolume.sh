#!/usr/bin/env bash

# Increment, decrement, or mute the volume and send a notification
# of the current volume level.

get_volume() {
	volume=$(pamixer --get-volume)
}

send_notification() {
	get_volume
	case $1 in 
	up_100)
		dunstify -a "changevolume" -u low -r 9993 -i "deaf" "Seriously You Fucking Deaf?"
		;;
	down_100)
		dunstify -a "changevolume" -u low -r 9993 -i "volume-mute" "You Know The Mute Button Exists Right?"
		;;
	*)
		dunstify -a "changevolume" -u low -r 9993 -h int:value:"$volume" -i "volume-$1" "Volume: ${volume}%" -t 2000
		;;
	esac
}


case $1 in
up)
	# Set the volume on (if it was muted)
	pamixer -u
	get_volume
	if [[ $volume == *100* ]]
	then
		send_notification "up_100" 
	else
		pamixer -i 5 --allow-boost
		send_notification "$1"
	fi
	;;
down)
	pamixer -u
	get_volume
	if [[ $volume == 0 ]]
	then
		send_notification "down_100"
	else
		pamixer -d 5 --allow-boost
		send_notification "$1"
	fi
	;;
mute)
	pamixer -t
	if eval "$(pamixer --get-mute)"; then
		dunstify -a "changevolume" -t 2000 -r 9993 -u low -i "volume-mute" "Muted"
	else
		send_notification up
	fi
	;;
esac