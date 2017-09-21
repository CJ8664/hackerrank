#!/usr/local/bin/python

# Problem URl : https://www.hackerrank.com/challenges/py-set-union/problem


count_one = int(raw_input().strip()) # No use

set_one = set(raw_input().strip().split())

count_two = int(raw_input().strip()) # No use

set_two = set(raw_input().strip().split())

set_union = set_one | set_two

print(len(set_union))
