$ Program URL : https://www.hackerrank.com/challenges/magic-square-forming

matrix = [
            [int(x) for x in raw_input().split(' ')],
            [int(y) for y in raw_input().split(' ')],
            [int(z) for z in raw_input().split(' ')]
         ]
mix_trans = -1
vals = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in xrange(3):
    if(sum(matrix[i])!=15):
        vals[2*(i + 1) + 1]+=1
        vals[2*(i + 1) + 2]+=1
        vals[2*(i + 1) + 3]+=1
        
for i in xrange(3):
    if((matrix[i][0] + matrix[i][1] + matrix[i][2])!=15):
        vals[3*i + 1]+=1
        vals[3*i + 2]+=1
        vals[3*i + 3]+=1

if((matrix[0][0] + matrix[1][1] + matrix[2][2])!=15):
    vals[1]+=1
    vals[5]+=1
    vals[9]+=1

if((matrix[0][2] + matrix[1][1] + matrix[2][0])!=15):
    vals[3]+=1
    vals[5]+=1
    vals[7]+=1    

n = vals.values()
y = max(n)

print(str(y/3))