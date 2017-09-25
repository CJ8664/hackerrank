#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

set_one_count = raw_input()
set_one = set(map(int,raw_input().strip().split()))

set_two_count = raw_input()
set_two = set(map(int,raw_input().strip().split()))

set_diff = set_one - set_two
print('{}'.format(len(set_diff)))
