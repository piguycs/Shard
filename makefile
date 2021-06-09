build: main.py
	@pyinstaller --onefile main.py
	clear
	@sudo ln -sf `pwd`/dist/main /usr/bin/shard
	@chmod +x /usr/bin/shard
	@sudo cp versions.json /usr/shard/versions/versions.json


test: /usr/bin/shard
	@shard -h

githubstuff: main.py loader.py
	@echo Starting the build
	@pyinstaller --onefile main.py

