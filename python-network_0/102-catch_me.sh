#!/bin/bash
# Script that makes a request to catch_me endpoint that returns "You got me!"
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
