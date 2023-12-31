# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 20:14:23 2023

@author: vikra
"""
import math

def circle_cal(radius):
    area = math.pi * radius * radius
    circumference=2*math.pi*radius
    diameter=2*radius
    return round(area,2), round(circumference,2), diameter
    
def main():
    radius = input("Enter Radius : ")
    radius = float(radius)
    area, c, r = circle_cal(radius)
    print(f" Area: {round(area,2)} ==> Circumference {c} ==> Diameter {r} ")
    
if __name__ == '__main__':
    main()
    