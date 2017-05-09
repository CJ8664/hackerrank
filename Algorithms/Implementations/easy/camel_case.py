# Program URL : https://www.hackerrank.com/challenges/camelcase

count = 1
sentence = raw_input().strip()
for char in sentence:
    if(ord(char)<97):
        count+=1
        
print(str(count))