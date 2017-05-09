Problem URL : https://www.hackerrank.com/challenges/divisible-sum-pairs

n,k = [int(x) for x in raw_input().strip().split(' ')]
a = [int(x) for x in raw_input().strip().split(' ')]

len_a = len(a)
i = 0
j = 0

counter = 0

while(i<len_a):
    j = i + 1
    while(j<len_a):
        if((a[i]+a[j])%k==0):
            counter+=1
        j+=1
    i+=1
    
print(str(counter))