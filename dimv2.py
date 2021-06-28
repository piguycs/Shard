#!/usr/bin/python3

from json import load
from requests import get
import ezjson

dims = ezjson.getfile("dimensions.json")

for x in dims["repos"]:
    print(x[0] +": "+ x[1])

repos = ["https://sparkofficial-1.ubuntulove2004.repl.co"]

# print(get(repos[0]+"/packs").json())
