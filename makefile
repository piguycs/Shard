build: main.py
	@pyinstaller --onefile main.py
	clear
	@sudo ln -sf `pwd`/dist/main /usr/bin/shard
	@chmod +x /usr/bin/shard


test: /usr/bin/shard
	@shard -h
