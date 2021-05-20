import sys
import json



class colors:
    GREEN_SUCCESS = '\033[1;32;40m'
    RESET = '\033[0;0;0m'


def doStuff(package):
    with open('usrfiles/package_list.json') as f:
        data = json.load(f)

    if package in data['packages']:
        print(colors.GREEN_SUCCESS + "[FOUND]" + colors.RESET + " Dependencies: {}".format(data['packages'][package]["depends"]))
    

def main(args):
    
    if len(args) == 1:
        print("No args given")
    else:
        for x in args:
            if args.index(x) == 0:
                print("hmmmmm sus")

            # Argument for help    
            elif x == '-h':
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
    print("Args: ", sys.argv)
    main(sys.argv)
