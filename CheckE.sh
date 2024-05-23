#!/bin/bash

g="$(grep -c Stationary $1)"
t="$(grep 'Free Energies' $1 | awk '{print $NF}')"

if [ $g -ne 2 ]
then
	echo "$1 failed to converge successfully."
	echo "Stationary was found $g time(s)."
else
	echo "$1 converged successfully"
	echo "Free Energy $t"
fi
