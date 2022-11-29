#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: 
#License: GNU/GPL 

import numpy as np
import matplotlib.pyplot as plt
import random as r

def createPoints():
    while True:
        p1, p2, p3 = (r.randint(-50, 50), r.randint(-50, 50)), (r.randint(-50, 50), r.randint(-50, 50)), (r.randint(-50, 50), r.randint(-50, 50))
        if p1 == p2 or p2 == p3 or p1 == p3:
            pass
        elif p1[0] == p2[0] and p2[0] == p3[0]:
            pass
        elif p1[1] == p2[1] and p2[1] == p3[1]:
            pass
        else:
            break
    return p1, p2, p3

def createCircle(r, center):
    segments = 50
    centerX = center[0]
    centerY = center[1]
    angle = np.linspace(0, 2*np.pi, segments+1)
    x = r * np.cos(angle) + centerX
    y = r * np.sin(angle) + centerY

    plt.plot(x, y, color='green', markersize=1)
    plt.plot(x, y, "bo")

    plt.title("Circles")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.gca().set_aspect("equal")
    plt.grid()
    plt.show()

def middlePoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def line(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    x = np.arange(-100, 100+0.1, 0.1)
    return m*(x-p1[0])+p1[1]

def mediatriz(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    m = -(1/m)
    x = np.arange(-100, 100+0.1, 0.1)
    point = middlePoint(p1, p2)
    return m*(x-point[0])+point[1]

def center(med1, med2, med3):
    for i in range(len(med1)):
        if med1[i] == med2[i]:
            if med3[i] == med2[i]:
                y = med1[i]
                x = i
                break
        else:
            print("Error")
    return [x, y]