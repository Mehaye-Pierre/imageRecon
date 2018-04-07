#!/bin/bash

if [ $# -ne 1 ]
	then
		echo "Donner fichier url en argument"
	else
		while read line  
		do
			./read_image $line
		done < $1
fi
