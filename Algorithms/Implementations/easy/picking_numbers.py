# Program URL : https://www.hackerrank.com/challenges/picking-numbers

num_input = int(raw_input().strip())
input_vals = map(int,raw_input().strip().split(' '))

val_dict = dict()

for val in input_vals:
    val_dict[val] = val_dict.get(val, 0) + 1

max_subset_len = 0

for val in val_dict.keys():
   
    listlen1 = 0
    listlen2 = 0
    
    listlen1+=val_dict.get(val, 0)
    listlen1+=val_dict.get(val-1, 0)
	
    listlen2+=val_dict.get(val, 0)
    listlen2=val_dict.get(val+1, 0)
    
    listlen = listlen1 if listlen1 > listlen2 else listlen2
    if(listlen>max_subset_len):
        max_subset_len=listlen
        
print(str(max_subset_len))