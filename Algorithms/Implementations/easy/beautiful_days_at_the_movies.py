# Program URL : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

i, j, k = [int(x) for x in raw_input().strip().split(' ')]

counter = 0
for num in xrange(i,j+1):
    if(abs(num-int(str(num)[::-1]))%k == 0):
        counter+=1
print(str(counter))