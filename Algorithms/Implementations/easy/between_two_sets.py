# Problem URL : https://www.hackerrank.com/challenges/between-two-sets

import sys

a = raw_input().strip().split(' ')
n = [int(x) for x in raw_input().strip().split(' ')]
m = [int(y) for y in raw_input().strip().split(' ')]

min_n = min(n)
max_m = max(m)

counter = 0
len_n = len(n)
len_m = len(m)

for i in xrange(min_n,max_m+1):
    cnt = 0
    for j in n:
        if(i%j==0): 
            cnt+=1
        else:
            break
    if(cnt==len_n): # All elements in A are factors of x
        cnt = 0
        for k in m:
            if(k%i==0): 
                cnt+=1
            else:
                break
        if(cnt==len_m):
            counter+=1
            
print(str(counter))