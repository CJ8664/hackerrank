# Program URL : https://www.hackerrank.com/challenges/the-love-letter-mystery

num_inputs = int(raw_input().strip())

for ip in xrange(num_inputs):
    ip_str = raw_input().strip()
    ops = 0
    ip_str_len = len(ip_str)
    for idx in xrange(ip_str_len/2):
        ops += abs(ord(ip_str[idx])-ord(ip_str[ip_str_len-idx-1]))
    print(str(ops))