#!/bin/bash

if [ "$1" == "" ]; then

    echo "Syntax: ./ip-sweep x.x.x"
    
else
    for IP in $(seq 1 254); do
    	ping -c 1 $1.$IP | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & #& multithreading
    done
fi
