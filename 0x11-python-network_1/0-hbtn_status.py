#!/usr/bin/python3
""" this module script that fetches https://intranet.hbtn.io/status """
import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()
    
with urllib.request.urlopen(req) as response:
    html1 = response.read().decode('utf-8')

print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8\
      content: {}".format(type(html), html, html1))

