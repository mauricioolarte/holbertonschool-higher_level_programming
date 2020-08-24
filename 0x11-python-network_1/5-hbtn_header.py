#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
