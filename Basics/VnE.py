#variables and expressions in Python
f=3
print f
f="abc"
print f

g=45

print "String" + str(g)

def functionname():
	global f
	f ="local value"
	print f

functionname()
print f

del f
print f
