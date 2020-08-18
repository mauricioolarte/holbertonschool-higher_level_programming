#!/usr/bin/env bash
#this show the size of dowload whit
acurl -so /dev/null $1 -w '%{size_download}\n'
