# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 17:05:06 2023

@author: vikra
"""

dic = {"China": 143, "India": 136, "USA": 36, "pakistan": 21}

print (dic)
while 1:
    userEnter = input("PLease Enter 1. Print, 2. Add, 3. Remove, 4.Query::  ")
    print (userEnter)
    userEnter = int(userEnter)
    
    if userEnter == 1:
        for x,v in dic.items():
            print (x, "==>",v)
    elif userEnter == 2:
        country = input("Enter Country to add: ")
        if country in dic:
            print(country, " already Exist")
        else:
             popu = input("Enter popu for the countery :")
             popu = int(popu)
             dic[country] = popu
        #print(dic)
    elif userEnter == 3:
        country = input("Enter Country to delete: ")
        if country in dic:
            del dic[country]
            for x,v in dic.items():
                print (x, "==>",v)
        else:
            print(country, " doesnt Exist")
        
        print(dic)
    elif userEnter == 4:
        inp = input("which countty Population u like to know: ")
        print(dic[inp])
    else:
        print ("Invalid  Value Exiting")
        break
    