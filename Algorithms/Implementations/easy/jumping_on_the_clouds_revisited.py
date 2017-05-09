# Program URL : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

jump_size = int(raw_input().strip().split(' ')[1])
clouds = [int(x) for x in raw_input().strip().split(' ')]

counter = 0
energy = 100
first = True

while(True):
    
    energy-=1
    counter = (counter + jump_size)%len(clouds)
    if(clouds[counter] == 1):
        energy-=2  
    if(first):
        first = False   
    if(counter == 0 and not first):
        break

print(str(energy))