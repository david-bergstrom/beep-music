#!/bin/bash

midicsv $1  | python2 parse.py | while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    f=$(awk -F',' '{print $1}' <<< "$line")
    s=$(awk -F',' '{print $2}' <<< "$line")
    d=$(awk -F',' '{print $3}' <<< "$line")

    beep -f $f -l $d
    sleep $s
    sleep 0.01
done
