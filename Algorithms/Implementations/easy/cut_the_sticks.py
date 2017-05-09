# Program URL : https://www.hackerrank.com/challenges/cut-the-sticks

n = int(raw_input().strip())
sticks = [int(x) for x in raw_input().strip().split(' ')]

while(len(sticks) > 0):
    print(len(sticks))
    min_stick = min(sticks)
    sticks = [stick-min_stick for stick in sticks if stick-min_stick > 0]