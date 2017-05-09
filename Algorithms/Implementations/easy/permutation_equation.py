# Program URL : https://www.hackerrank.com/challenges/permutation-equation

num_ele = raw_input()
elements = [int(x) for x in raw_input().strip().split(' ')]
ele_map = dict()
for ele in elements:
    ele_map[elements[elements[ele-1]-1]-1]=ele-1
    
for ele in xrange(len(elements)):
    print(str(ele_map[ele]+1))