#!/usr/local/bin/python

# Problem URL https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())

    print("".join([str(x) for x in xrange(1,n+1)]))
