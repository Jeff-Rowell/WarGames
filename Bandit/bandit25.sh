#!/bin/bash

pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for i in `seq -w 9999`; do
	echo $pass $i
	echo $pass $i | nc localhost 30002 >> results.txt &
	sleep 1
done
