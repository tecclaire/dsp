#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:39:17 2017

@author: tecclaire
"""
import csv

with open('faculty.csv','r') as csvfile:
    read_csv = csv.reader(csvfile)
    next(read_csv)
    
    def get_dict(st):
        values = []
        lname = []
        for row in st:
            name = tuple(row[0].split())
            values.append(row[1:])
            lname.append(name)
        dict_list = {n:v for n, v in zip(lname, values)}
        return dict_list
   

       # dict_list ={k: data_dict[k] for k in sorted(data_dict.keys())[:2]}
      #  print {k: dict_list[k] for k in sorted(data_dict.keys())[:2]}
    print (get_dict(read_csv))