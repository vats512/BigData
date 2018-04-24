#!/usr/bin/env python

import sys
import string

key = None
currentkey = None
weekends = 0
weekdays =0
weekend = [5, 6, 12, 13, 19, 20, 26, 27]
for line in sys.stdin:
        line = line.strip()
        key,dates = line.split("\t",1)
        date = int(dates)
        if key == currentkey:
                if date in weekend:
                        weekends = weekends + 1
                else:
                        weekdays = weekdays +1
        else:
                if currentkey == None: #First time
                        if date in weekend:
                                weekends = weekends + 1
                        else:
                                weekdays = weekdays +1                      
                else:
                        avg_we = float(weekends/8.0)
                        avg_wd = float(weekdays/23.0)
                        print("{0:s}\t{1:.2f}, {2:.2f}".format(str(currentkey),avg_we,avg_wd))
                        if date in weekend:
                                weekends = 1
                                weekdays = 0
                        else:
                                weekdays = 1
                                weekends = 0                       
                currentkey = key
#for the last key

avg_we = float(weekends/8.0)
avg_wd = float(weekdays/23.0)
print("{0:s}\t{1:.2f}, {2:.2f}".format(str(currentkey),avg_we,avg_wd))
