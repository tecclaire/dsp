#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:39:17 2017

@author: tecclaire
"""
import csv

emails = ['bad','dog','cat']

def write_to_csv(list_of_emails):
    with open ('emails.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['Emails'])
        f_csv.writerows([x.split() for x in list_of_emails])
        return f_csv

print (write_to_csv(emails))

for item in emails:
    print (item)