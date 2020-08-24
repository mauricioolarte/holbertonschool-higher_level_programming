#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        html = response.info()
    
        print(html['X-Request-Id'])
