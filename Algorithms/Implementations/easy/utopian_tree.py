# Program URL : https://www.hackerrank.com/challenges/utopian-tree

for counter in xrange(int(raw_input().strip())):
    cycles = int(raw_input().strip())
    if(cycles==0):
        print('1')
    elif (cycles%2==0):
        print(str(2**((cycles/2)+1) - 1))
    else:
        print(str(2**((cycles/2)+2) - 2))