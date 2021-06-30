#!/usr/bin/python3

from requests import get
from ezjson import setCfg as conf
from output import out

dims = conf("dimensions.json")

# Gets all the items from the array, index one coz 2d array
# so these are all the repo url's
repos = dims.getAll("repos", 1)
# and this will get repo names
reponames = dims.getAll("repos", 0)

for x in repos:
    packageList = [reponames[repos.index(x)]]
    if x != "none":
        packages = get(x+"/packs").json()
        for y in packages:
            try:
                # print(y["name"] + " " + (y["url"] if y["url"] != '' else "BITCH URL MISSING"))
                packageList.append(y["name"])
            except KeyError:
                print(y["name"] + " --> ERR: URL TAG MISSING")

find = "pain"


if find in packageList:
    print(out("[FOUND]", 1) + f' Package {find} in {packageList[0]}')
