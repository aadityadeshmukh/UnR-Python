def main():
	x=0
	print "While"
	while(x<5):
		print x
		x+=1

	print "For -- Range"
	for x in range(5,10):
		print x

	print "For -- set "
	days = ["Mon", "Tue", "Wed","Thu", "Fri", "Sat", "Sun"]
	for d in days:
		print d

	print "for -- getting the value and iterator"
	for i, d in enumerate(days):
		print i, d
if __name__ == "__main__":
	main()