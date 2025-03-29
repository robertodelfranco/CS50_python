import sys
import os

def main():
	if (len(sys.argv) != 1):
		print("Usage: python virtual_environment.py")
		sys.exit(1)
	try:
		if os.environ['VIRTUAL_ENV']:
			print("Virtual environment active")
	except KeyError:
		print("Virtual environment inactive")


if __name__ == '__main__':
	sys.exit(main())