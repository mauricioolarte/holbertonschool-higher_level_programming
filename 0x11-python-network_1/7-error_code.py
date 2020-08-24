#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code < 400:
        print(req.status_code)
    else:
        print('Error code: {}'.format(req.status_code))
