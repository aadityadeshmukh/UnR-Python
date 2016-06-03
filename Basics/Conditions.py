def main():
	x=10000
	y=100
	if(x>y):
		print "x greater than y"
	elif x < y:
		print "y greater than x"
	else:
		print "x equals y"

	st = "yo: x  is greater" if x>y else "yo:y is greater or number equal"
	print st

if __name__ == "__main__":
	main()