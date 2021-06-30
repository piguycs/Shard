#!/usr/bin/python3

from requests import get
from ezjson import setCfg as conf
from output import out

dims = conf("dimensions.json")

repos = dims.getAll("repos", 1)

packageList = []
for x in repos:
    if x != "none":
        packages = get(x+"/packs").json()
        for y in packages:
            try:
                # print(y["name"] + " " + (y["url"] if y["url"] != '' else "BITCH URL MISSING"))
                packageList.append(y["name"])
            except KeyError:
                print(y["name"] + " --> ERR: URL TAG MISSING")

if "pain" in packageList:
    print(out("[FOUND]", 1) + out("pain in repo", 4))
