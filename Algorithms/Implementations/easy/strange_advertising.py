# Problem URL : https://www.hackerrank.com/challenges/strange-advertising

import math

days = int(raw_input().strip())
total_people = 2
people = 2

for i in xrange(1,days):
    people = math.floor(people*1.5)
    total_people +=people
    
print(str(int(total_people)))