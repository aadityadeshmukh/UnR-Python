def main():
    f=open("textfile.txt", "w+") #Open a file in write mode. if absent, create = w+
    for i in range(0,10):
        f.write("Line number %s \n" % str(i+1))

    f2=open("textfile.txt", "a+") #Open a file in append mode. if absent, create a+
    for i in range(10,20):
       f2.write("Line number is %s \n" % str(i+1))
    f.close()

    f=open("textfile.txt", "r") # read file as a whole
    if(f.mode == 'r'):
        strn = f.read()
    print strn

    if(f.mode == 'r'): # read file line by line
        fl = f.readlines()
        for x in fl:
            print x

if __name__ == "__main__":
    main()