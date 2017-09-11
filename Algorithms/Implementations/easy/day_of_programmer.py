#!/bin/python

# Problem URL : https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import sys

def solve(year):
    
    dayOfProgrammer = ''
    
    if year == 1918:
        return '26.09.1918'
    
    # Julian Calendar
    if year < 1918:
        if year % 4 == 0: # Leap year
            dayOfProgrammer = '12.09.' + str(year)
        else:
            dayOfProgrammer = '13.09.' + str(year)
    else:
        if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0): # Leap year
            dayOfProgrammer = '12.09.' + str(year)
        else:
            dayOfProgrammer = '13.09.' + str(year)   
    return dayOfProgrammer 

year = int(raw_input().strip())
result = solve(year)
print(result)
