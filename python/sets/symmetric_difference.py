#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/symmetric-difference/problem

num_ele_first_set = raw_input()
first_set = set(map(int,raw_input().strip().split()))
num_ele_second_set = raw_input()
second_set = set(map(int,raw_input().strip().split()))

result_set = first_set.union(second_set) - first_set.intersection(second_set)

for x in sorted(list(result_set)):
    print(str(x))

