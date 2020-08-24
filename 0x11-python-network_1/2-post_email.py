#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    params = urllib.parse.urlencode({'email': sys.argv[2]})
    params = params.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], params) as response:
        print(response.read().decode('utf-8'))
