#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Send OPTIONS request to the server using curl
response=$(curl -s -X OPTIONS -i "$1")

# Extract and display allowed HTTP methods from the response
allowed_methods=$(echo "$response" | grep -i "Allow:" | awk '{print $2}')
echo "Allowed HTTP methods for $1 are: $allowed_methods"
