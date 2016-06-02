# Funtions in Python
def func1():
	print "Yo m a function"

def func2(arg1,arg2):
	print arg1, "" ,arg2

def cube(arg1):
	return arg1*arg1*arg1

def power(arg1, arg2=1):
	result = 1
	for i in range(arg2):
		result = result * arg1
	return result

def multi_add(*args):
	result = 0
	for i in args:
		result = result + i
	return result
func1()
print func1()
print func1

func2(10,20)
print func2(10,20)

print cube(7)
print power(5,3)
print power(arg2=4, arg1 = 3)
print multi_add(1,2,3,4)