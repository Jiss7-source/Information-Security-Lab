#!/bin/bash
echo "enter filename"
read filename

if [ ! -f "$filename" ]
then
	echo "file not found."
	exit 1
fi
hashfile=$filename.hash

if [ ! -f $hashfile ]
then
	sha256sum "$filename">"$hashfile"
	echo "hash created,file is now being monitored"
else
	sha256sum -c "$hashfile"

fi
 
