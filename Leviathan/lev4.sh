#!/bin/bash

x="01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010"

for a in $x; do printf "%x" $((2#$a)); done | xxd -r -p
printf "\n"
