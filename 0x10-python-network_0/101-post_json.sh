#!/bin/bash
#jason files whit post
curl -X POST -H "Content-Type: application/json" -d@"$2" "$1"
