# Program URL : https://www.hackerrank.com/challenges/mars-exploration

ip_str = raw_input().strip()
count = 0
idx = 0
while(idx<len(ip_str)-2):    
    if(ip_str[idx]!='S'):count+=1
    if(ip_str[idx+1]!='O'):count+=1
    if(ip_str[idx+2]!='S'):count+=1
    idx+=3
print(str(count))