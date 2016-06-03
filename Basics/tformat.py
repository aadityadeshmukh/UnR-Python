from datetime import date
from datetime import time
from datetime import datetime

def main():
	now = datetime.now()

	print now.strftime("%Y")
	print now.strftime("%y")

	print now.strftime("%a, %d, %B, %y") # a -- day, d  -- number, B -- month, y -- year
	print now.strftime("%c, %x, %X")

	print now.strftime("%I:%M:%S %p") # 1 hour clock, minutes, seconds, am/pm
	print now.strftime("%H:%M")
	
if __name__ == "__main__":
	main()