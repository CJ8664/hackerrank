# Program URL : https://www.hackerrank.com/challenges/taum-and-bday

num_tests = int(raw_input().strip())

for cunter in xrange(num_tests):
    units_b,units_w = [long(x) for x in raw_input().strip().split(' ')]
    cost_b,cost_w,cost_ex = [long(x) for x in raw_input().strip().split(' ')]
    
    if(cost_b == cost_w): # No use of exchange
        print(str(cost_b * units_b + cost_w * units_w))
    elif(cost_b > cost_w): # Check if black can be converted
        if(cost_b > (cost_w + cost_ex)): # Conversion is cheaper
            print(str((cost_w + cost_ex) * units_b + cost_w * units_w))
        else:
            print(str(cost_b * units_b + cost_w * units_w))
    else:
        if(cost_w > (cost_b + cost_ex)): # Conversion is cheaper
            print(str(cost_b * units_b + (cost_b + cost_ex) * units_w))
        else:
            print(str(cost_b * units_b + cost_w * units_w))