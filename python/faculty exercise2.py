#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:39:17 2017

@author: tecclaire
"""
import csv
import re


csvfile = open('faculty.csv')
readcsv = csv.reader(csvfile)


def count_titles(csv_file_name):
    next(csv_file_name)
    title = []
    for row in csv_file_name:
        title.append(row[2])
    
    if 'Assistant Professor is Biostatistics' in title:
        loc = title.index('Assistant Professor is Biostatistics')
        title[loc] = str('Assistant Professor of Biostatistics')
    
    titlecount = {x:title.count(x) for x in title}
    print (titlecount.values())
    
count_titles(readcsv)