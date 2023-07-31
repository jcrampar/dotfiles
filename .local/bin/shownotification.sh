#!/bin/sh


eachTime=15
while true 
do
    currentMinute=$(date +"%M")
    isShowed=false
    if ! (( 10#$currentMinute % $eachTime )) ; then
        sh ~/.local/bin/showdatenotification.sh
        #echo "Hello word"
        isShowed=true
    fi
    if $isShowed ; then
        sleep 900
    else 
        sleep 60
    fi
done
