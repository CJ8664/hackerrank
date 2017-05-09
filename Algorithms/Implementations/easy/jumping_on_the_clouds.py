# Problem URL : https://www.hackerrank.com/challenges/jumping-on-the-clouds

num_clouds = int(raw_input().strip())
clouds = [int(x) for x in raw_input().strip().split(' ')]

index = 0
jumps = 0
while(True):
    
    if((index+2) <= (num_clouds - 1) and clouds[index+2] == 0):
        index+=2
    else:
        index+=1
    jumps+=1
    
    if(index >= num_clouds - 1):
        break
        
print(str(jumps))