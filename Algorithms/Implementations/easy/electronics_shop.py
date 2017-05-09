# Program URL : https://www.hackerrank.com/challenges/electronics-shop

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = [int(x) for x in input().strip().split(' ') if int(x) < s]
pendrives = [int(x) for x in input().strip().split(' ') if int(x) < s]

max_exp = -1

for keyboard in keyboards:
    for pendrive in pendrives:
        if(keyboard+pendrive <= s):
            if(keyboard+pendrive>max_exp):
                max_exp = keyboard+pendrive

print(str(max_exp))  