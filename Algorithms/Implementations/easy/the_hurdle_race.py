# Program URL : https://www.hackerrank.com/challenges/the-hurdle-race

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
heights = [int(x) for x in raw_input().strip().split(' ') if int(x) > k]

if(len(heights) == 0):
    print('0')
elif (len(heights) == 1):
    print(str(heights[0]-k))
else:
    heights.sort()
    print(str(heights[len(heights)-1]-k))