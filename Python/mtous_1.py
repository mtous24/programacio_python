# mtous_1
from math import*
def f1(angle):
    angle = angle*pi/180
    y = 4 + sin(angle)
    return y
def f2(angle):
    angle = angle*pi/180
    y = 4 + 230 * sin(angle)
    return y


for angle in range(45, 360+1):
    y1 = f1(angle)
    y2 = f2(angle)
    
    print(angle, y1)
    print(" ")
    print(angle, y2)