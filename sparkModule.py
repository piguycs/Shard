from requests import get
from os import popen as run
from json import load, dumps
from loader import Loader

url = "https://api.github.com/repos/HUSKI3/Spark/releases/latest"
latestVer = get(url).json()["name"].split(' ')[2]

def checkFile(file):
    return 1 if 'y' in run(f'if test -f {file}; then echo y; fi').read() else 0

def parseVersion(version):
    realVersion = ''
    for x in version:
        if x.isdigit():
            realVersion = realVersion + x

    return realVersion

def getCurrVer():
    with open("versions.spark") as f:
        currVer = load(f)["current"]
        return currVer

def sparkVersions(check):
    if not checkFile("versions.spark") and check:
        run("touch versions.spark")
    elif not check:
        return 1

class getSpark:
    def __init__():
        sparkVersions(1)     # Creates a version file if not present
        if parseVersion(latestVer) > parseVersion(getCurrVer()):
            sparkurl = get(url).json()["assets"][0]["browser_download_url"]
            with Loader("Installing latest version of spark  ", "Installing latest version of spark   ✔"):
                run("wget -q -O spark.py {}".format(sparkurl))

            with open("versions.spark", "w") as f:
                f.write(dumps('{"current": "{}"}'.format(latestVer), indent=4, sort_keys=True))


