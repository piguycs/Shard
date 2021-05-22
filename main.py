import sys, os, json, ast

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
    versions = os.popen("sudo spark -nv {}".format(package)).read()
    versions = ast.literal_eval(versions)
    
    return versions

def versionManagement(pkgName):

    versions = getUpdates(pkgName)
    
    # TESTING STUFF
    # currVersion = int(''.join([v for v in package['version'].split(".")]))
    
    
    currVersion = versions["installed"]
    latestVersion = versions["latest"]
    
    # Doing a check here as a failsafe
    # checking for installed packages is done beforehand in function doStuff() which is faster
    if currVersion != False:
        print(colors.GREEN_SUCCESS + "[FOUND]" + colors.RESET +
            " Installed version: {}".format(currVersion))
        if currVersion < latestVersion:
            print(colors.YELLOW_INFO + "[UPDATE]" + colors.RESET +
                " LATEST version: {}".format(latestVersion))
    else:   
        print(colors.RED_FAILURE + "[NOT FOUND]" + colors.RESET +
              " The package you searched for is not present")




def doStuff(package):
    with open(files.INSTALLED_JSON) as f:
        data = json.load(f)

    if package in data['packages']:
        versionManagement(package)
    else:
        print(colors.RED_FAILURE + "[NOT FOUND]" + colors.RESET +
              " The package you searched for is not present")
    

def main(args):
    
    if len(args) == 1:
        print("No args given")
    else:
        for x in args:
            if args.index(x) != 0:

                # Argument for help    
                if x == '-h':
                    print(
                        colors.GREEN_SUCCESS + "[ARG: {}]".format(x) + 
                        colors.RESET + " Shard is an open source package manager for spark, which is an open source package installer")

                elif x == '-v':
                    print(colors.GREEN_SUCCESS + "[ARG: {}]".format(x) +
                        colors.RESET + " My creator was tatching hentai so he forgot to give me a version".format(x))
                
                elif x == '-dog':
                    print(colors.GREEN_SUCCESS + "[ARG: {}]".format(x) +
                        colors.RESET + " Bow wow, time to kill.sh".format(x))
                
                else: doStuff(x)



if __name__ == '__main__':
    file_exists = False

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

    main(sys.argv) if file_exists else None
