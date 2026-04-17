import sys
def greet():
	print("Hello! Welcome to the Python Executable Demo.")

def main():
	try:
		greet()
		name = input("Enter your name: ")
		print(f"Hello, {name}! Have a great day!")
	except Exception as e:
		print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
	main()

# 1. Install pip
> sudo apt install python3-pip

# 2. Install virtual environment support
> sudo apt install python3-venv

# 3. Install PyInstaller using pip
> python3 -m pip install pyinstaller


> python3 -m PyInstaller --onefile main.py

> cd dist
> ./g1
