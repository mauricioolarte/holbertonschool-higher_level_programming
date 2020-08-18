#!/usr/bin/env bash
#this show the size of dowload whit curl
curl $1 -w '%{size_request} bytes\n'
