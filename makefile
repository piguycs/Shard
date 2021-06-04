build: main.py
	@pyinstaller --onefile main.py
	clear
	@sudo ln -sf `pwd`/dist/main /usr/bin/shard
	@chmod +x /usr/bin/shard


test: /usr/bin/shard
	@shard -h

githubstuff: main.py loader.py
	@echo Starting the build
	@pyinstaller --onefime main.py

