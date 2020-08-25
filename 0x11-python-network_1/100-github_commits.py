#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/" + owner + "/" + repo + "/commits"
    req = requests.get(url)
    answ = req.json()
    j = 0
    for i in answ:
        while j < 10:
            print("{}: {}".format(answ[j]['sha'],
                  answ[j]["commit"]["author"]["name"]))
            j = j + 1
