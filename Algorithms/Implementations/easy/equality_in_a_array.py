# Program URL : https://www.hackerrank.com/challenges/equality-in-a-array

num_elements = int(raw_input().strip())
elements = [int(x) for x in raw_input().strip().split(' ')]

ele_dict = dict()
for ele in elements:
    ele_dict[ele] = ele_dict.get(ele, 0) + 1
	
print(str(num_elements-max(ele_dict.values())))