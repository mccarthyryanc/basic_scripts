#!/bin/bash
#
#script to repeat provided command. Example:
#
#   $ ./repeat.sh 4 play -q sound.mp3
#
#   will repeat the command "play -q sound.mp3" 4 times.
#

maxtimes="$1";
shift;
cmd="$@";

for ((i = 1; i <= $maxtimes; i++ ));
do 
    eval "$cmd";
done 
