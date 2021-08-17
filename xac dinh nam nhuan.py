# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:47:00 2021

@author: anhtrannh
"""
num = int(input("Enter year number: "))
if num % 400 == 0:
    print(num,"la nam nhuan")
elif num % 4 == 0 and num % 100 != 0:
    print(num,"la nam nhuan")
else:
    print(num,"la nam khong nhuan")
