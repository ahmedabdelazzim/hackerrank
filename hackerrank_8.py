#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:06:39 2018

@author: ahmedabdou
"""


if __name__=='__main__':
    t=int(input())
    data ={}
    for i in range(1,t+1): 
        x=input()
        data[x.split()[0]]= int(x.split()[1])
    
    while True:  
        try: 
            y=input()
            print(y +"="+ str(data[y]))
        except EOFError:
            break
        except:
            print ("Not found")
       
        