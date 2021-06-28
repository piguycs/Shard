from json import load

def getfile(file):
    with open(file) as f:
        file = load(f)
    return file