import os
from os import path
import datetime
from datetime import date, time,timedelta
import time
def main():
    #print the name of the os
    print os.name

    #Check for item existence and type
    print "Item exists: " + str(path.exists("textfile.txt"))
    print "Item is a file: "+ str(path.isfile("textfile.txt"))
    print "Item is a directory: " + str(path.isdir("textfile.txt"))

    #Check for the full path of the item
    print "The full path of the item is: " + str(path.realpath("textfile.txt"))
    print "The path and the name of the item is: " + str(path.split(path.realpath("textfile.txt")))

    #Check for the modified time of the file
    print "The file was modified at: " + str(path.getmtime("textfile.txt"))
    print "The file size is:" + str(path.getsize("textfile.txt"))
    
    mt = time.ctime(path.getmtime("textfile.txt"))
    print mt
    print datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))

    #Finding the time elapsed for the file mod
    tNow=datetime.datetime.now()
    tElapsed = tNow - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print "The file was modified: %s or" % tElapsed
    print str(tElapsed.total_seconds()) + " seconds ago"



if __name__ == "__main__":
    main()