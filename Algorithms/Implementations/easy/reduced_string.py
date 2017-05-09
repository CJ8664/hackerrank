# Program URL : https://www.hackerrank.com/challenges/reduced-string

small_string = raw_input().strip()

i = 0
while(i<len(small_string)-1):
    if(small_string[i]==small_string[i+1]):
        small_string=small_string[0:i] + small_string[i+2:]
        i = 0
    else:
        i+=1

if(len(small_string)>0):
    print(small_string)
else:
    print('Empty String')