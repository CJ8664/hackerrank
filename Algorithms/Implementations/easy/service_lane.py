# Program URL : https://www.hackerrank.com/challenges/service-lane

num_tests = int(raw_input().strip().split(' ')[1])
service_width = [int(x) for x in raw_input().strip().split(' ')]

for i in xrange(num_tests):
    entry, exit = [int(x) for x in raw_input().strip().split(' ')]
    print(str(min(service_width[entry:exit+1])))