class myClass():
	def method1(self):
		print "myClass::Method 1"
	def method2(self,str):
		print "myclass::method2 says " ,str

class derived(myClass):
	def method1(self):
		print "derived::method1"
	def method2(self):
		print "yo m always all the way up!"

def main():
	obj = myClass()
	obj.method1()
	obj.method2("yo m all the way up!")

	obj1 = derived()
	obj1.method1()
	obj1.method2()

if __name__ == "__main__":
	main()