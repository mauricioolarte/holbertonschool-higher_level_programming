#!/bin/bash
#return status code
curl -s -o /dev/null "$1" -w "%{response_code}"
