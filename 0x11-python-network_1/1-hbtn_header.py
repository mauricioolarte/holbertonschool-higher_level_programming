#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.info()
    dict = html.__dict__

    print(dict['_headers'][-2][1])
