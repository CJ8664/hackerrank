# Program URL : https://www.hackerrank.com/challenges/designer-pdf-viewer

heights = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

if(len(word) == 0):
    print('0')
if(len(word) == 1):
    print(str(heights[ord(word[0])-97]))
else:
    max_height = 0
    for ch in word:
        if(heights[ord(ch)-97]>max_height):
            max_height = heights[ord(ch)-97]
    print(str(max_height*len(word)))