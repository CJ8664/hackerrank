#!/usr/local/bin/python

# Problem URL https://www.hackerrank.com/challenges/sherlock-and-array/problem

import sys

def solve(a):
    
    total = sum(a)
    left_sum = 0
    right_sum = total - a[0]
    
    if left_sum == right_sum:
        return 'YES'
    
    for i in xrange(1, len(a)):
        
        left_sum += a[i-1]
        right_sum -= a[i]
        
        if left_sum == right_sum:
            return 'YES' 
    return 'NO'

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)
