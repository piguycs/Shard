buildnrun: main.py
	@pyinstaller --onefile main.py
	clear
	@./dist/main
	@sudo ln -sf `pwd`/dist/main /usr/bin/shard
	@chmod +x /usr/bin/shard


run:
	@./dist/main
