Problem URL : https://www.hackerrank.com/challenges/breaking-best-and-worst-records

n = int(raw_input().strip())
score = [int(x) for x in raw_input().strip().split(' ')]

min = score[0]
max = score[0]

i = 1
min_c = 0
max_c = 0
while(i < n):
    a = score[i]
    if(a>max):
        max=a
        max_c+=1
    if(a<min):
        min=a
        min_c+=1
    i+=1

print(str(max_c) + ' ' + str(min_c))