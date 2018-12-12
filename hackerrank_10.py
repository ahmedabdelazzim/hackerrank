#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:35:31 2018

@author: ahmedabdou
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    x = []
    y = []
    c =1
while n>0 :
    rem = n%2
    n=math.floor(n/2)
    x.append(rem)    

for i in range(0,len(x)-1):    
    if x[i] == x[i+1]:
        c=c+1
        y.append(c)
    elif x[i] != x[i+1]:
        y.append(c)
        c=1

m=max(y)
print(m)