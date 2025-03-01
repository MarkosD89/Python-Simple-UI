#!/bin/bash

directory=Data              # directory to generate new data

if [ -d $directory ]        # Check if Directory exists
then
    echo "directory exist: $directory"
else                        # if directory not exist -> create directory                        
    echo "directory did not exist: $directory"
    mkdir $directory        
    echo "new directory was created: $directory"
fi

myvarx=1   # Device Cords X
myvary=1   # Device Cords Y

while [ $myvarx -le 5 ]
do
    while [ $myvary -le 5 ]
    do
        # Create CSV file for the current combination of myvarx and myvary for a map
        filename="$directory/$myvarx.$myvary.csv"
        touch "$filename"
        
        # Column Names Time and Signal
        echo "Time,Signal" > "$filename"

        for t in $(seq 0 0.1 10)
        do
            Signal=$(awk "BEGIN {print $myvary + $myvarx + $t}")       # Create a signal
            echo "$t,$Signal" >> "$filename"                 # Add this to the file
        done
        # Increment myvary for the next loop
        myvary=$((myvary + 1))
        if [ $? -eq 0 ]
        then
            echo "Data was generated correctly $filename"
        else
            echo "We were not able to generate the data properly"
        fi
    done
    myvarx=$((myvarx + 1))
    myvary=1            # Reset myvary for the next round
done