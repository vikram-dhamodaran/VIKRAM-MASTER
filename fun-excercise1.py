# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:54:02 2023

@author: vikra
"""

def cal_area(prm1, prm2, stype="Triangle"):
    if stype == "rectangle":
        area = prm1*prm2
    else:
        area = (1/2)*prm1*prm2
    return area

base = 2
height = 5
stype = "rectangle"
area_of_shape = cal_area(base, height, stype)
print("area of Rectangle: ", area_of_shape)

base = 3
height = 10

area_of_shape = cal_area(base, height, stype)
print("area of Triangle: ", area_of_shape)

area_of_shape = cal_area(base, height)
print("area of Triangle default shape: ", area_of_shape)
    