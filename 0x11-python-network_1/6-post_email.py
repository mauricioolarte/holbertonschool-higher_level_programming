#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import sys
import requests

if __name__ == "__main__":
    arguments = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], arguments)
    print(req.text)
