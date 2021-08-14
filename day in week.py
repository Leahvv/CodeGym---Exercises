# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:33:06 2021

@author: anhtrannh
"""

daylis = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,\
          "Saturday":6,"Sunday":7}
day = int(input ("Enter your day:"))
if day == 1:
	print("Monday")
elif day == 2:
	print("Tuesday")
elif day == 3:
	print("Wednesday")
elif day == 4:
	print("Thursday")
elif day == 5:
	print("Friday")
elif day == 6:
	print("Saturday")
elif day == 7:
	print("Sunday")
else:
    print("Error, out of range")