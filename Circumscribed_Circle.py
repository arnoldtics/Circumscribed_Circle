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

points = createPoints()
print(points)