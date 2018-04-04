#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 11:33:23 2017

@author: tecclaire
"""
import csv

with open('faculty.csv','r') as csvfile:
    readcsv = csv.reader(csvfile)
    next(readcsv)
    dictlist = {}
    for lines in readcsv:
        name, degree, title, email = lines
        dictlist[name] = degree,title,email
    print (dictlist)