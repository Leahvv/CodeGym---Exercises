# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 08:19:29 2021

@author: anhtrannh
"""

import turtle
import random as r

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, -200)
t.speed(10)
t.pensize(5)
t.pencolor("blue")
t.circle(400)

t.penup()
t.speed(10)
t.shape("turtle")
t.pencolor('green')
t.goto(0, 0)

angle = random.randint(0, 360)
t.right(angle)
t.showturtle()

count = 0
while True:
    t.speed(1)
    t.forward(188)
    t.hideturtle()
    t.speed(10)
    t.goto(0, 0)
    angle = random.randint(0, 360)
    t.right(angle)
    t.showturtle()
    count += 1
    if count == 10:
        break

turtle.done()