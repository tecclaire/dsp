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


def emails(csv_file_name):
    next(csv_file_name)
    em = []
    for row in csv_file_name:
        em.append(row[3])
    em=str(em).lower()
    
    email = re.findall('[a-z0-9.%_+-]+@[a-z0-9.-]+\.[a-z]{2,4}',em)
    return email

a = emails(readcsv)


def unique_domains(ema):
    ema = str(ema)
    domains = re.findall(r'[a-z0-9.%_+-]+@([a-z0-9.-]+\.[a-z]{2,4})', ema)
    return set(domains)

print (unique_domains(a))
