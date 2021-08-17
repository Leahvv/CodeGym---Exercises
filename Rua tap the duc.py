# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 08:19:29 2021

@author: anhtrannh
"""

import turtle
import random as r

t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.pensize(4)
t.color("blue")
t.speed(1)
t.penup()
t.goto(-400,0)
t.showturtle()

count = 0
while count < 10:
    down = r.randint(20, 50)
    up = r.randint(20,50)
    t.pendown()
    t.forward(down)
    t.penup()
    t.forward(up)
    count = count + 1
turtle.done()