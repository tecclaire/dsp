#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:20:11 2017

@author: tecclaire
"""

import csv

    
# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Don't use pandas.

# Following functions will be called like this:
#   footballTable = read_data('football.csv')
#   minRow = get_index_with_min_abs_score_difference(footballTable)
#   print str(get_team(minRow, footballTable))

def read_data(filename):
    with open (filename, 'r') as f:
        f_csv = csv.reader(f)
        next(f_csv)
    
        data_list=[]
    
        for row in f_csv:
            data_list.append(row)
        
        return data_list

    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
footballTable = read_data('football.csv')

def get_index_with_min_abs_score_difference(parsed_data):
    goals = [x[5] for x in parsed_data]
    goalsallowed = [x[6] for x in parsed_data]
    diff = [abs(int(x) - int(y)) for x,y in zip(goals,goalsallowed)]
    whoindex = diff.index(min(diff))
    return whoindex
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index"""
    
   
minRow = get_index_with_min_abs_score_difference(footballTable)    

def get_team(index_value, parsed_data):
    who = parsed_data[int(index_value)][0]
    return who
    #Returns the team name at a given index.
    """
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """

print(get_team(minRow,footballTable))