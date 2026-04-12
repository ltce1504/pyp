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
