# Program URL : https://www.hackerrank.com/challenges/minimum-distances

num_ele = int(raw_input().strip())
elements = [int(x) for x in raw_input().strip().split(' ')]
ele_dict = dict()
counter = 0
for ele in elements:
    if(ele_dict.get(ele, 0) == 0): # First time entry
        ele_dict[ele] = counter
    else:
        ele_dict[ele] = ele_dict.get(ele, 0) - counter
    counter+=1
if(len(ele_dict.keys()) == num_ele):
    print('-1')
else:
    min_dist = num_ele - 1
    for ele in ele_dict.keys():
        if(ele_dict[ele] < 0):
            ele_dict[ele] = -1 * ele_dict[ele]
            if(ele_dict[ele] < min_dist):
                min_dist = ele_dict[ele]
    print(str(min_dist))