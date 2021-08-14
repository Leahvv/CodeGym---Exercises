# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:40:51 2021

@author: anhtrannh
"""

num = int(input("Give me a price: "))
if num >= 150:
	print("Total: ", num - 50)
elif num >= 100:
	print("Total: ", num - 25)
elif num >= 75:
	print("Total: ", num - 15)
else:
    print("Total: ", num)