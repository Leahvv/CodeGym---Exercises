# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 08:13:19 2021

@author: anhtrannh
"""

import turtle
a = int(input("Enter number: "))
r = turtle.Turtle()
r.hideturtle()
r.pencolor("blue")
edge = 0
while edge < 4:
    r.forward(a)
    r.right(90)
    edge = edge + 1
turtle.done()