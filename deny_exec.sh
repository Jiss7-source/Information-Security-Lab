#!/bin/bash
echo "enter filename:"
read filename

if [ -f "$filename" ]
then
	chmod -x "$filename"
	echo "execution permission denied to $filename"
else
	echo "$filename doesn't exist"
fi

