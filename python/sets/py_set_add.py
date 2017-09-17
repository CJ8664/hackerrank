#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/py-set-add/problem

countries = set()
for i in xrange(int(raw_input().strip())):
    countries.add(raw_input().strip())
    
print len(countries)
