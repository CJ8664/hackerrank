# Program URL : https://www.hackerrank.com/challenges/alternating-characters

for itr in xrange(int(raw_input().strip())):
    # For every test case
    counter = 0
    incr = 1
    delete = 0
    ip_str = raw_input().strip()
    while(counter < len(ip_str) - incr):
        if(ip_str[counter] == ip_str[counter + incr]): # Delete the next char
            delete+=1
            incr+=1
        else:
            counter = counter + incr
            incr = 1
    print(str(delete))