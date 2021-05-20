buildnrun: main.py
	@pyinstaller --onefile main.py
	clear
	@./dist/main


run:
	@./dist/main
