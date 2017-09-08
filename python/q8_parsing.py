# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

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
