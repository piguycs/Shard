import sys

class colors:
    GREEN_SUCCESS = '\033[1;32;40m'
    RESET = '\033[0;0;0m'


def doStuff(package):
    print(package)
    print("we downloaded it dw just dont use it yet its installing for the next 500 years")

def main(args):
    
    if len(args) == 1:
        print("No args given")
    else:
        for x in args:
            if args.index(x) == 0:
                print("nothin")

            # Argument for help    
            elif x == '-h':
                print(
                    colors.GREEN_SUCCESS + "[ARG: {}]".format(x) + 
                    colors.RESET + " Shard is an open source package manager for spark, which is an open source package installer"
                )

            elif x == '-v':
                print("[ARG: {}] My creator was tatching hentai so he forgot to give me a version".format(x))
            elif x == '-dog':
                print("[ARG: {}] Bow wow, time to kill.sh".format(x))
            else: doStuff(x)  



if __name__ == '__main__':
    print("Args: ", sys.argv)
    main(sys.argv)
