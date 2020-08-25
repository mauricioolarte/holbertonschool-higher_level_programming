#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(username, token))
    answ = req.json()
    print(answ.get('id'))
