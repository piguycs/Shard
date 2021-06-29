#!/usr/bin/python3

from requests import get
from ezjson import setCfg as conf

dims = conf("dimensions.json")

repos = dims.getAll("repos", 1)

for x in repos:
    print(get(x+"/packs").json() if x != "none" else "None")
# print(get(repos[0]+"/packs").json())
