#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    req = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        answ = req.json()
        if answ == {}:
            print("No result")
        else:
            print('[{}] {}'.format(answ.get('id'), answ.get('name')))
    except ValueError as error:
        print("Not a valid JSON")
