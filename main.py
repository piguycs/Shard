from sys import argv
from os import system, popen, geteuid, path
from json import load
from requests import get, post

from spark import install, getPkg, update as updatedim
from loader import Loader
from sparkModule import getSpark
from output import out

# from styles/themes.py import colours


# IDK why I did this but welkom to classitown
class configs:
    CHECK_UPDATES = True

class globalArgs:
    DEBUG_MODE = False
    USE_SPARK = True
    UPDATE = False

class files:
    INSTALLED_JSON = '/usr/spark/installed.json'
    VERSIONS = '/usr/shard/versions/versions.json'
    CFG = '/usr/shard/config.json'



# Requires spark
def getUpdates(package):
    with Loader("Checking into the dimensions ", "Checking into the dimensions ✔"):
        versions = getPkg(package)
        print(versions)
    
    return versions

# fml
# redundent function
def parseVersion(versionNumber):
    realVersion = ''
    for x in versionNumber:
        if x.isdigit():
            realVersion = realVersion + x

    return float(realVersion)


def update(pkgName):
    if input("Do you wanna update? [y/N] ") in ['y','Y']:
        binDir = popen("which {}".format(pkgName)).read()
        if binDir != '':
            system("sudo cp {} /tmp/shard".format(binDir))
            try:
                # system("sudo spark -i {}".format(pkgName))
                install(pkgName)
            except:
                system("sudo cp /tpm/shard {}".format(binDir))
        else:
            warnFiles = input("There seem to be no local files present for the package, do you stll wanna install [y/N]")
            if warnFiles in ['y','Y']:
                install(pkgName)


def versionManagement(pkgName):

    versions = getUpdates(pkgName)
    
    # TESTING STUFF
    # currVersion = int(''.join([v for v in package['version'].split(".")]))

    currVersion = str(versions["installed"])
    latestVersion = str(versions["latest"])

    # not using these lolol
    # displayVersionCurr = versions["installed"]
    # displayVersionLatest = versions["latest"]


    # Doing a check here as a failsafe
    # checking for installed packages is done beforehand in function doStuff() which is faster
    if currVersion != False:
        print(out("[FOUND]", 1) + " Installed version: {}".format(currVersion))
        if currVersion != latestVersion:
            print(out("[UPDATE]", 3) + " LATEST version: {}".format(latestVersion))
            
            update(pkgName)
            updatedim()

    else:   
        print(out("[NOT FOUND]", 2) + " The package you searched for is not present")




def doStuff(package, update):
    if package != None:
        with open(files.INSTALLED_JSON) as f:
            data = load(f)

        if package in data['packages']:
            versionManagement(package)
        elif popen("which {}".format(package)).read():
            print(out("[WARN]", 3) + " The package you searched for present but not installed using spark")
        else:
            print(out("[NOT FOUND]", 2) + " The package you searched for is not present")
    else:
        print("shard shard real smooth")
    
    

def main(args):

    if len(args) > 1:
        package = args[-1] if args[-1] != "shard" else None
        
        if "-h" in args:
            print(out("[ARG: {}]".format("-h"), 1) + " Shard is an open source package manager for spark, which is an open source package installer")
        elif "-v" in args:
            print(out("[ARG: {}]".format("-v"), 1) + " My creator was tatching hentai so he forgot to give me a version")
        elif "-dog" in args:
            print(out("[ARG: {}]".format("-dog"), 1) + " Bow wow, time to kill.sh")
        elif "-y" in args:
            # TBD
            doStuff(package, True)
        else:
            doStuff(package, False)
    else:
        print("No args given")
     

def versions():
    version = get("https://api.github.com/repos/RocKing1001/Shard/releases/latest").json()

    try:
        with open(files.VERSIONS) as f:
            version = load(f)["latest"]
            return version
    except IOError:
        return 0




def loadConfigs():
    with open(files.VERSIONS) as f:
        configs.CHECK_UPDATES = load(f)["checkUpdates"]


if __name__ == '__main__':
    # getSpark()

    # loads configs
    loadConfigs()

    # print(configs.CHECK_UPDATES)
    
    
    file_exists = False
    
    system("mkdir /tmp/shard") if not path.isdir("/tmp/shard") else None
    
    try:
        with open('/usr/spark/installed.json') as f:
            files.INSTALLED_JSON = '/usr/spark/installed.json'
            file_exists = True
    except IOError:
        print("SPARK IS NOT INSTALLED")

    version = versions()

    if geteuid() != 0:
        print("Run this command with \'sudo\'")
    else:
        main(argv) if file_exists else None
