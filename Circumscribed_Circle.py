#!/usr/bin/env python3
#Author: Arnoldo Fernando Chue Sánchez
#Contact: 
#License: GNU/GPL 

import numpy as np
import matplotlib.pyplot as plt
import random as r

def createPoints():
    while True:
        p1, p2, p3 = (r.randint(-100, 100), r.randint(-100, 100)), (r.randint(-100, 100), r.randint(-100, 100)), (r.randint(-100, 100), r.randint(-100, 100))
        if p1 == p2 or p2 == p3 or p1 == p3:
            pass
        elif p1[0] == p2[0] and p2[0] == p3[0]:
            pass
        elif p1[1] == p2[1] and p2[1] == p3[1]:
            pass
        elif (p2[1]-p1[1])/(p2[0]-p1[0]) == (p3[1]-p2[1])/(p3[0]-p2[0]):
            pass
        else:
            break
    return p1, p2, p3

def createCircle(r, center):
    segments = 1000
    centerX = center[0]
    centerY = center[1]
    angle = np.linspace(0, 2*np.pi, segments+1)
    x = r * np.cos(angle) + centerX
    y = r * np.sin(angle) + centerY
    return x, y

def middlePoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def euclideanNorm(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def line(p1, p2):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p1[1]-(m*p1[0])
    return m*x+b

def mediatriz(p1, p2):
    m = -(1/((p2[1]-p1[1])/(p2[0]-p1[0])))
    point = middlePoint(p1, p2)
    b = point[1]-(m*point[0])
    return m*x+b

def center(p1, p2, p3):
    point1 = middlePoint(p1, p2)
    point2 = middlePoint(p2, p3)
    m1 = -(1/((p2[1]-p1[1])/(p2[0]-p1[0])))
    m2 = -(1/((p3[1]-p2[1])/(p3[0]-p2[0])))
    b1 = point1[1]-(m1*point1[0])
    b2 = point2[1]-(m2*point2[0])
    return ((b1-b2)/(m2-m1), m1*((b1-b2)/(m2-m1))+b1)

if __name__ == "__main__":
    points = createPoints()
    p1, p2, p3 = points[0], points[1], points[2]
    x = np.linspace(-100, 100, 100)
    line1, line2, line3 = line(p1, p2), line(p2, p3), line(p1, p3)
    circuncenter = center(p1, p2, p3)
    circle = createCircle(euclideanNorm(p1, circuncenter), circuncenter)
    xCircle, yCircle = circle[0], circle[1]

    fig, ax = plt.subplots(figsize=(20,20))
    ax.plot(x, line1, color="blue")
    ax.plot(x, line2, color="red")
    ax.plot(x, line3, color="green")
    ax.plot(xCircle, yCircle, color="black")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Circumscribed Circle")
    fig.set_facecolor("lightsteelblue")
    plt.grid()
    plt.show()