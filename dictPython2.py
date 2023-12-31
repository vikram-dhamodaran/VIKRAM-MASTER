# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:53:42 2023

@author: vikra
"""
import statistics

stocks = {"info": [600,630,620], 
         "ril":[1430,1490,1567],
         "mtl":[234,180,160]
    }


def printall():
    for u, v in stocks.items():
        avg= statistics.mean(v)
        print(f"{u}==>{v}==>avg: ",round(avg,2))
        
def Add():
    stock = input("Enter stock to add: ")
    p = input("Enter price of this stock:")
    p = float(p)
    if stock in stocks:
        print(stock, " already Exist")
        stocks[stock].append(p)
    else:
         stocks[stock] = [p]
         
    printall()
def main():
    op = input("Enter Operation : 1) Print 2) Add or amend : ")
    if(op.lower() == "print"):
        printall()
    elif(op.lower() == "add"):
        Add()
    else:
        print("invalid Option")
        
    
if __name__ == '__main__':
    main()