#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:12:50 2019

@author: ahmedabdou
"""


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    flat_arr = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    x=len(arr[0]) -1
    y=len(arr) - 2
    a=0; b=1; c=2; j=0;
    m= arr[j][a] + arr[j][b] + arr[j][c] \
              + arr[j+1][b] + arr[j+2][a] + arr[j+2][b] + arr[j+2][c]; 
    while j<y:
        a=0; b=1; c=2;
        while c<=x:
            s = arr[j][a] + arr[j][b] + arr[j][c] \
              + arr[j+1][b] + arr[j+2][a] + arr[j+2][b] + arr[j+2][c]
            a+=1; b+=1; c+=1;
            if s > m:
                m=s
        j+=1;
    print(m)   


