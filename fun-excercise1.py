# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:54:02 2023

@author: vikra
"""

def cal_area(base, height):
    area = (1/2)*base*height
    return area

base = 2
height = 5

area_triangle = cal_area(base, height)

print("area of Triange: ", area_triangle)