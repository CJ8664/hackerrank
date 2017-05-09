# Problem URL : https://www.hackerrank.com/challenges/fair-rations


num_sub = int(raw_input().strip())
breads = map(int,raw_input().strip().split(' '))

if (num_sub == 2 and sum(breads)%2 != 0):
    print('NO')
else:
    bread_dist = 0
    for i in xrange(1, num_sub-1):

        if((i-1) > 0 and breads[i-1]%2 != 0):
            breads[i-1]+=1
            breads[i]+=1
            bread_dist+=2
        elif((i+1) < num_sub and breads[i+1]%2 != 0):
            breads[i+1]+=1
            breads[i]+=1
            bread_dist+=2
                
        print(str(sum([1 if x%2 == 0 else 0 for x in breads])))
        if(sum([1 if x%2 == 0 else 0 for x in breads]) == num_sub):
            print(str(bread_dist))
            break
            
    if(sum([1 if x%2 == 0 else 0 for x in breads]) != num_sub):
        print('NO')
        