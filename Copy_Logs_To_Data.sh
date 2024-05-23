#!/bin/bash

cont=$1

for i in *.log; do
	if [ -d "/u/af/ao/${username}/Data/$cont" ]; then
		cp $i /u/af/ao/${username}/Data/$cont
	else	
		mkdir /u/af/ao/bpayton/Data/$cont
		echo "$cont directory created."
		cp $i /u/af/ao/bpayton/Data/$cont
	fi
done
