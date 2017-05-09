# Program URL : https://www.hackerrank.com/challenges/angry-professor

num_test_cases = int(raw_input().strip())
for inputs in xrange(num_test_cases):
    k = int(raw_input().strip().split(' ')[1])
    if(len([int(x) for x in raw_input().strip().split(' ') if int(x) <= 0]) >=k):
        print('NO')
    else:
        print('YES')