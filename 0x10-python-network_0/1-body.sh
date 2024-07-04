#!/bin/bash
# sends a GET request to a URL, and displays the body of the response only if the status code is 200
curl -sL -w "%{http_code}" "$1" -o temp.txt | { read status; [ "$status" -eq 200 ] && cat temp.txt; }

