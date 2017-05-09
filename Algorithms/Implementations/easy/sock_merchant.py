# Program URL : https://www.hackerrank.com/challenges/sock-merchant

n = int(raw_input().strip())
socks = map(int,raw_input().strip().split(' '))

sock_histogram = dict()

for sock in socks:
    sock_histogram[sock] = sock_histogram.get(sock, 0) + 1

total = 0
for sock in sock_histogram.keys():
    total+=sock_histogram[sock]/2
    
print(str(total))