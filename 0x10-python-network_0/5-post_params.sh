#!/bin/bash
#post whit arguments.
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
