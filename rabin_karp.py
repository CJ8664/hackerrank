act_str = 'abaaababaaabababaaaaababababbababababbaababaaabababababaaabaab'
sub_str = 'abaa'

char_map = dict()

i = 0
sub_str_hash = 0
act_str_hash = 0

for c in sub_str:
    if(c not in char_map.keys()):
        char_map[c] = ord(c)-96
    
    sub_str_hash += char_map[c] * 3**i
    act_str_hash += char_map[act_str[i]] * 3**i
    
    i+=1
if(sub_str_hash==act_str_hash):
    print('Match')
    
j = 0
while(j < len(act_str)-len(sub_str)):
    act_str_hash = (act_str_hash - char_map[act_str[j]])/3 + char_map[act_str[j+len(sub_str)]] * 3**(len(sub_str)-1)
    if(act_str_hash==sub_str_hash):
        print('Match')
    j+=1