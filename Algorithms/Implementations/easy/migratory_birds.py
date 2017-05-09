# Program URL: https://www.hackerrank.com/challenges/migratory-birds

bird_histogram = {1:0, 2:0, 3:0, 4:0, 5:0}

n = int(raw_input().strip())
birds = [int(x) for x in raw_input().strip().split(' ')]

for bird in birds:
    bird_histogram[bird] = bird_histogram[bird] + 1
    
max_bird = bird_histogram[1] 
max_type = 1

for i in xrange(2,6):
    if(bird_histogram[i] > max_bird):
        max_type = i
        max_bird = bird_histogram[i]
        
print(str(max_type))