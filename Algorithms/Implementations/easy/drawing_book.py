# Program URL : https://www.hackerrank.com/challenges/drawing-book

n = int(raw_input().strip())
p = int(raw_input().strip())

if(n==p or p==1):
    print('0')
elif(n%2!=0): # Even number of page
    if(p<=n/2.0):
        print(str(p/2))
    else:
        print(str((n-p)/2))
else:    
    if(p<=n/2.0):
        print(str(p/2))
    else:
        if(p%2==0):
            print(str((n-p)/2))
        else:
            print(str((n-p)/2 + 1))


n = int(raw_input().strip())
p = int(raw_input().strip())

if(n==p or p==1):
    print('0')
elif(p<=n/2.0):
    print(str(p/2))
elif(n%2!=0): # Even number of page
    print(str((n-p)/2))
else:    
    if(p%2==0):
        print(str((n-p)/2))
    else:
        print(str((n-p)/2 + 1))