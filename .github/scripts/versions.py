from requests import get, post

version = get("https://api.github.com/repos/RocKing1001/shard/releases/latest").json()["name"].split(' ')[1].split('.')
versionParsed = {
    "release": version[0],
    "beta": version[1],
    "alpha": version[2]
}



print(versionParsed)