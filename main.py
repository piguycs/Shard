import sys, os, json, ast
from loader import Loader

class globalArgs:
    DEBUG_MODE = False
    USE_SPARK = True
    UPDATE = False

class files:
    INSTALLED_JSON = ''

class colors:
    GREEN_SUCCESS = '\033[1;32m'
    RED_FAILURE = '\033[1;31m'
    YELLOW_INFO = '\033[1;33m'
    GREY_INFO = '\033[30;47m'
    RESET = '\033[0;0;0m'


# Requires spark
def getUpdates(package):
    with Loader("Checking into the dimensions ", "Checking into the dimensions ✔"):
        versions = os.popen("sudo spark -nv {}".format(package)).read()
        versions = ast.literal_eval(versions)
    
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
        binDir = os.popen("which {}".format(pkgName)).read()
        if binDir != '':
            os.system("sudo cp {} /tmp/shard".format(binDir))
            try:
                os.system("sudo spark -i {}".format(pkgName))
            except:
                os.system("sudo cp /tpm/shard {}".format(binDir))
        else:
            print("There seem to be no local files present for the package")


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
        print(colors.GREEN_SUCCESS + "[FOUND]" + colors.RESET +
              " Installed version: {}".format(currVersion))
        if currVersion != latestVersion:
            print(colors.YELLOW_INFO + "[UPDATE]" + colors.RESET +
                  " LATEST version: {}".format(latestVersion))
            
            update(pkgName)

    else:   
        print(colors.RED_FAILURE + "[NOT FOUND]" + colors.RESET +
              " The package you searched for is not present")




def doStuff(package, update):
    if package != None:
        with open(files.INSTALLED_JSON) as f:
            data = json.load(f)

        if package in data['packages']:
            versionManagement(package)
        elif os.popen("which {}".format(package)).read():
            print(colors.YELLOW_INFO + "[WARN]" + colors.RESET +
                " The package you searched for present but not installed using spark")
        else:
            print(colors.RED_FAILURE + "[NOT FOUND]" + colors.RESET +
                " The package you searched for is not present")
    else:
        print("shard shard real smooth")
    
    

def main(args):

    if len(args) > 1:
        package = args[-1] if args[-1] != "shard" else None
        
        if "-h" in args:
            print(colors.GREEN_SUCCESS + "[ARG: {}]".format("-h") + 
                colors.RESET + " Shard is an open source package manager for spark, which is an open source package installer")
        elif "-v" in args:
            print(colors.GREEN_SUCCESS + "[ARG: {}]".format("-v") +
                colors.RESET + " My creator was tatching hentai so he forgot to give me a version")
        elif "-dog" in args:
            print(colors.GREEN_SUCCESS + "[ARG: {}]".format("-dog") +
                colors.RESET + " Bow wow, time to kill.sh")
        elif "-y" in args:
            # TBD
            doStuff(package, True)
        else:
            doStuff(package, False)
    else:
        print("No args given")
     



if __name__ == '__main__':
    file_exists = False
    
    os.system("mkdir /tmp/shard") if not os.path.isdir("/tmp/shard") else None
    
    try:
        with open('usrfiles/package_list.json') as f:
            files.INSTALLED_JSON = 'usrfiles/package_list.json'
            file_exists = True
    except IOError:
        try:
            with open('/usr/spark/installed.json') as f:
                files.INSTALLED_JSON = '/usr/spark/installed.json'
                file_exists = True
        except IOError:
            print("SPARK IS NOT INSTALLED")

    if os.geteuid() != 0:
        print("Run this command with \'sudo\'")
    else:
        main(sys.argv) if file_exists else None
