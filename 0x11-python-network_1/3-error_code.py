#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
