# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:07:30 2021

@author: anhtrannh
"""
dai = int(input("nhap chieu dai: "))
rong = int(input("nhap chieu rong: "))
for row in range(dai):
    for col in range(rong):
        if (col==0) or (col==rong-1) or ((row==0 or row==dai-1) and (col>0 and col <rong-1)):
            print("*",end="")
        else:
            print(end=" ")
    print()

