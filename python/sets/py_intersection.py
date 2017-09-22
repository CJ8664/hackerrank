#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

set_one_cnt = raw_input()

set_one = set(map(int, raw_input().strip().split()))

set_two_cnt = raw_input()

set_two = set(map(int, raw_input().strip().split()))

set_intersection = set_one & set_two

print(len(set_intersection))

