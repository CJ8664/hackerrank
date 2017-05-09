# Program URL : https://www.hackerrank.com/challenges/find-digits

num_inputs = int(raw_input().strip())
for inputs in xrange(num_inputs):
    num_str = raw_input().strip()
    num = int(num_str)
    counter = 0
    for digit in num_str:
        if(digit != '0'):
            if(num%int(digit) == 0):
                counter+=1
    print(str(counter))