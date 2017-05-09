# Program URL : https://www.hackerrank.com/challenges/cats-and-a-mouse

q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = [int(num) for num in raw_input().strip().split(' ')]
    print('Cat A' if abs(x-z) < abs(y-z) else 'Cat B' if abs(x-z) > abs(y-z) else 'Mouse C') 