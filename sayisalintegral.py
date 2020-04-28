#!/usr/bin/python3.5
#-*- coding: utf-8 -*-

def f(x):
    return(x**2+2)

a,b = 1,3
n = 2
integral = 0

h = (b-a)/n

for i in range(n):
    integral += (f(a+i*h) + f(a+(i+1)*h))*h/2

print(integral)

