#!/bin/bash
echo "enter filename:"
read filename
if [ -f "$filename" ]
then
        sha256sum "$filename" > hash.txt
        echo "hash stored in hash.txt"
        echo "checking integrity"
        sha256sum -c hash.txt
else
        echo "$filename not found."
fi