#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/no-idea/problem

sizes = raw_input() # No USE
moods = dict()

for mood in raw_input().strip().split():
    moods[int(mood)] = moods.get(int(mood), 0) + 1
    
happy = set(map(int, raw_input().strip().split()))
sad = set(map(int, raw_input().strip().split()))
    
happiness = 0

for mood, value in moods.items():
    if mood in happy:
        happiness += value
    elif mood in sad:
        happiness -= value
        
print(str(happiness))
