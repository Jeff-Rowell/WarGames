#!/bin/bash

for i in `seq -w 9999`; do
	echo "Trying $i...."
	~/leviathan6 $i
	sleep .5
done
