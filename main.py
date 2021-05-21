import sys
import json

class files:
    INSTALLED_JSON = ''

class colors:
    GREEN_SUCCESS = '\033[1;32;40m'
    RED_FAILURE = '\033[1;31;40m'
    YELLOW_INFO = '\033[1;33;40m'
    RESET = '\033[0;0;0m'


def versionManagement(package):
    currVersion = (package['version'])

    # TESTING STUFF
    newVersion = (v for v in package['version'].split("."))
    
    print(colors.GREEN_SUCCESS + "[FOUND]" + colors.RESET +
          " Installed version: {}".format(currVersion))
    print(colors.YELLOW_INFO + "[UPDATE]" + colors.RESET +
          " LATEST version: {}".format(newVersion))




def doStuff(package):
    with open(files.INSTALLED_JSON) as f:
        data = json.load(f)

    if package in data['packages']:
        versionManagement(data['packages'][package])
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

    print("SHARD BOOTING UP")
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
