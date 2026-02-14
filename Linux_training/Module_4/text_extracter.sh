#!/bin/bash

#check no.of cmd args
if [ "$#" -ne 1 ]; then
    echo "Input File Not Given"
    exit 1
fi

input="$1"
output="output.txt"

#clears o/p file by redirecting nothing to it
> "$output"

#setting internal field sep empty so that it doesnt split on spaces
while IFS= read -r line; do

    if [[ "$line" == *"\"frame.time\""* ]]; then
        echo "$line" >> "$output"

    elif [[ "$line" == *"\"wlan.fc.type\""* ]]; then
        echo "$line" >> "$output"

    elif [[ "$line" == *"\"wlan.fc.subtype\""* ]]; then
        echo "$line" >> "$output"
        echo "" >> "$output"
    fi

done < "$input"

echo "Output saved to $output"

