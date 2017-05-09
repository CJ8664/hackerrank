# Program URL : https://www.hackerrank.com/challenges/the-birthday-bar

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]

if(n==1 and s[0]==d):
    print(str(1))
else:
    i = 0
    counter = 0
    while(i<n-m+1):
        if(sum(s[i:i+m])==d):
            counter+=1
        i+=1
    print(str(counter))