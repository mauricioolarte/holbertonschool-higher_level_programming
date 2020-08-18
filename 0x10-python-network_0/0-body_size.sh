#!/bin/bash
#this show the size of dowload whit
curl -so /dev/null "$1" -w '%{size_download}'
