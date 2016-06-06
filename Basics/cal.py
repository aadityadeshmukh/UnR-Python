import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2016, 6 , 0 , 0)
#print str

for i in c.itermonthdays(2016, 7):
    print i
    
for name in calendar.month_name:
    print name

for day in calendar.day_name:
    print day
    
#Monthly meeting

for m in range(1, 13):
    mc = calendar.monthcalendar(2016, m)
    week1 = mc[0]
    week2 = mc[1]
    
    if week1[calendar.WEDNESDAY] != 0:
        meetday = week1[calendar.WEDNESDAY]
    else:
        meetday = week2[calendar.WEDNESDAY]
   
    print "%10s %2d" % (calendar.month_name[m], meetday)