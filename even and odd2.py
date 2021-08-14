# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:29:37 2021

@author: anhtrannh
"""

num = input("Enter your number:")
num_ = float(num)
if num_ % 2 == 0:
    print("Even")
elif num_ % 2 == 1:
    print("Odd")
else:
    print("not a natural number")
