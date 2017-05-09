# Program URL : https://www.hackerrank.com/challenges/two-characters

s_len = int(raw_input().strip())
ip_str = raw_input().strip()

char_dict = dict()

for char in ip_str:
    char_dict[char] = char_dict.get(char, 0) + 1

dist_chars = char_dict.keys()
max_len = -1
for i in xrange(len(dist_chars)):
    for j in xrange(i+1, len(dist_chars)):
        if(abs(char_dict[dist_chars[i]] - char_dict[dist_chars[j]]) <= 1):
            new_str = ''.join([char if (char in dist_chars[i]+''+dist_chars[j]) else '' for char in ip_str])
            counter = 0
            sym = True
            while(counter < len(new_str) - 2):
                if(new_str[counter] != new_str[counter+2]):
                    sym = False
                    break
                counter+=2
            if(sym):
                if(len(new_str) > max_len):
                    max_len = len(new_str)
if(max_len != -1):                  
    print(str(max_len))
else:
    print('0')