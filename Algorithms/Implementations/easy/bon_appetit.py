# Program URL : https://www.hackerrank.com/challenges/bon-appetit

annas_bill = 0.0

skipped_item = int(raw_input().strip().split(' ')[1])

items = [float(x) for x in raw_input().strip().split()]

i = 0
while(i < len(items)):
    if(i!=skipped_item):
        annas_bill+=items[i]/2.0
    i+=1
   
anna_charged = float(raw_input().strip())
if(anna_charged!=annas_bill):
    print(str(int(anna_charged-annas_bill)))
else:
    print('Bon Appetit')