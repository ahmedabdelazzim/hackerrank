#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:08:18 2018

@author: ahmedabdou
"""

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if self.age<0: 
            self.age=0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the               console
        if self.age<13:
            print("You are young.") 
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        elif self.age >=18:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here      
        self.age=self.age+1