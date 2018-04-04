#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:20:11 2017

@author: tecclaire
"""

import csv

with open('football.csv') as csvfile:
    readcsv = csv.reader(csvfile)
    next(readcsv)
    
    teams = []
    goals = []
    goalsallowed = []
    
    for row in readcsv:
        team = row[0]
        goal = row[5]
        goalallowed = row[6]
        
        teams.append(team)
        goals.append(goal)
        goalsallowed.append(goalallowed)
    csvfile.close
 
zipg = zip(goals,goalsallowed)
diff = [abs(int(x) - int(y)) for x,y in zipg]
whoindex = diff.index(min(diff))
who = teams[int(whoindex)]

print (who)