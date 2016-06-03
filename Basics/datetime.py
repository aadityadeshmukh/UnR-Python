from datetime import date
from datetime import time
from datetime import datetime

def main():
	today = datetime.today()
	print today

	print today.day
	print today.month
	print today.year

	now = datetime.now()
	print now

	t = datetime.time(datetime.now())
	print t

	wd = date.weekday(today)
	day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	print "Today is " , day[wd]
	
if __name__ == "__main__":
	main()