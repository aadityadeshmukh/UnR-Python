from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

#Santa Tracker
today = date.today()
print "Today is " + str(today)
christmas = date(today.year, 12, 25)
if today > christmas:
   christmas(today.year + 1)

print "Santa will visit in " + str (abs (christmas - today)) 


print timedelta(days = 365, hours = 5, minutes = 2)
print "One year from now it will be " + str (datetime.now() + timedelta(365))
print "Three weeks from now it will be " + str (datetime.now() + timedelta (weeks = 3))
print "1 week before today it was " + str (datetime.now() - timedelta( weeks = 1))