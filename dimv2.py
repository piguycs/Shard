#!/usr/bin/python3

from json import load
from requests import get
import ezjson

repos = []
dims = ezjson.getfile("dimensions.json")

for x in dims["repos"]:
    print(x[0] +": "+ x[1])
    repos.append(x[1])
print(repos)
for x in repos:
    print(get(x+"/packs").json()) if x != "none" else None
# print(get(repos[0]+"/packs").json())
