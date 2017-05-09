# Program URL : https://www.hackerrank.com/challenges/repeated-string

ip_str = raw_input().strip()
num_chars = long(raw_input().strip())

counter = 0
for char in ip_str:
    if(char == 'a'):
        counter+=1
        
mul = int(num_chars/len(ip_str))
rem = num_chars-(mul*len(ip_str))

counter = mul * counter

for char in ip_str[:rem]:
    if(char == 'a'):
        counter+=1
        
print(str(counter))