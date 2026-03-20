
#!/bin/bash

count=1
echo "S.No | File Name | Creation Date"
echo "-------------------------------"

for file in *
do
	 if [ -f  "$file" ]
	 then
		date=$(stat -c %y "$file"| cut -d' ' -f1)
		echo "$count. $file - $date"
		((count++))
	 fi
done

