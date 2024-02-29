#!/bin/bash

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request to the URL with custom header using curl
response=$(curl -s -X GET -H "X-School-User-Id: 98" "$1")

# Display the body of the response
echo "Response body:"
echo "$response"
