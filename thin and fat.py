# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:43:17 2021

@author: anhtrannh
"""

height = int(input("Enter your height:"))
weight = int(input("Enter your weight:"))

bmi = weight / (height * 2)
print("Your BMI: ", bmi)

if bmi < 16:
    print("Thin level III")
elif bmi >= 16 and bmi < 17:
    print("Thin level II")
elif bmi >= 17 and bmi < 18.5:
    print("Thin level I")
elif bmi >= 18.5 and bmi < 25: 
    print("Normal")
elif bmi >= 25 and bmi < 30: 
    print("Fat")
elif bmi >= 30 and bmi < 35: 
    print("Fat level I")
elif bmi >= 35 and bmi < 40:
    print("Fat level II")
else: 
    print("Fat level III")