#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# URL to send DELETE request
URL=$1

# Send DELETE request and display response body
curl -X DELETE -sSL "$URL"
