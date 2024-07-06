#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me to get the message "You got me!" in the response.
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
