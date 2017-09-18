#!/usr/local/bin/python

# Problem URL https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = input()
s = set(map(int, raw_input().split())) 
for i in xrange(int(raw_input().strip())):
    ip = raw_input().strip().split()
    cmd = ip[0]            
    if cmd == "pop":
        s.pop()         
    elif cmd == "remove":
        ele = int(ip[1])
        s.remove(ele)
    elif cmd == "discard":
        ele = int(ip[1])
        s.discard(ele)        
print(str(sum(s)))

