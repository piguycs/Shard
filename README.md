# Shard

A simple, fast and beautiful package manager designed to work with spark

This is a no garbage package manager which is based on top of spark for installing and removing packages. (WARNING: EXTREMLY WIP USE AT YOUR OWN RISK)

## How to use
To check for a package do:
```bash
sudo shard {package}
```
Shard is meant to be working on its own but due to the state of the app right now, it is advisable to use spark. 


## What does "no garbage" mean?
Glad you asked, it means it wont spout unnecessary nonsense at your screen with logs you dont need. They will be saved in a logfile and if they are really needed shard will parse them to be as simple as they can be. However because spark is in-dev and thats what I use to install and modify packages, logs are enabled for now.
