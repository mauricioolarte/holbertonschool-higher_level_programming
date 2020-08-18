#!/bin/bash
#show allows
curl -sI "$1" | grep Allow | cut -d":" -f2 | cut -c2-
