#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:39:17 2017

@author: tecclaire
"""
import csv
import re


with open('faculty.csv') as csvfile:
    readcsv = csv.reader(csvfile)
    next(readcsv)
    
    degrees = []
    titles = []
    emails = []
    
    for col in readcsv:
        deg = col[1].split(" ")
        for d in deg:
            degrees.append(d)
  
print (deg)