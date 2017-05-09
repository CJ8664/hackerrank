# Problem URL : https://www.hackerrank.com/challenges/counting-valleys

x = raw_input()
counter = 0
valleys = 0
is_valley = False

for x in raw_input().strip():
    if(counter==0):
        if(x=='U'):
            is_valley = False
        else:
            is_valley = True

    if(x=='U'):
        counter+=1
    else:
        counter-=1

    if(counter==0 and is_valley):
        valleys+=1

print(str(valleys))