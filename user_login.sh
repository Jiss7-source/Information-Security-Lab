#!/bin/bash
echo "Enter username:"
read username
while true
do
	if who| grep -w "$username" >/dev/null
	then 
		echo "user $username is logged in"
		break
	else
		echo "user $username was not logged in.checking again in 30 seconds"
		sleep 30
	fi 
	
done

