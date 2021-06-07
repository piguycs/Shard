from os import popen

def checkFile(file):
    try:
        with open(file) as f:
            return 1
    except IOError:
        return 0

if __name__ == "__main__":
    if checkFile('/usr/shard/versions/versions.json'):
        popen("sudo mkdir /usr/shard")
        popen("sudo mkdir /usr/shard/versions")
