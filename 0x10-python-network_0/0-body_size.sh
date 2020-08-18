#!/bin/bash/env bash
#this show the size of dowload whit curl
curl -so /dev/null $1 -w '%{size_request} bytes\n'
