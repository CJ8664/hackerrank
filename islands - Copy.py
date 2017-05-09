# Problem url: https://www.hackerrank.com/challenges/letter-islands

import math

length = 0
numisl = 0
a = ''
size = 0
maxlen = 0
subs = dict()

def getNumIsland(s):

    da = a
    flag = 1
    ls = int(len(s))
    i = 0
    #print(s)
    while(True):
        for j in xrange(ls):
            if(a[i+j]!=s[j]):
                #print('mismatch',i,j,a[i+j],s[j])
                flag = 0
                break
            else:
                flag = 1
        if(flag == 1): # Substring match
            flag = 0
            da = da[0:i] + ("x"*ls) + a[i+ls:] # try to replace char at index
            #print(da)  
        else:
            flag = 1
        i+=1
        if(i+ls>length):
            break
  
    count = 0       
    flag = 1
    #print(s,da)
    for n in xrange(length):
        if(da[n]=='x' and flag == 1):
            count+=1
            if(count > numisl):
                return False
            flag = 0
        elif(da[n]!='x'):
            flag = 1
    
    if(count==numisl):
        return True
    else:
        return False

def runProcess():  

    global length, numisl, size, a
    finalcnt = 0
    for i in xrange(length):
        for j in xrange(length):
            if(j+size>length):
                break
            s = a[j:j+size]
            if s not in subs:
                subs[s] = 0
                # check here is the number of islands are 
                if(getNumIsland(s)):
                    #print(s)
                    finalcnt+=1 
        size+=1
        if(size>maxlen):
            break
    print(str(finalcnt))   
    
def main():

    global length, numisl, size, a, subs, maxlen
    a = raw_input().strip()
    
    length = len(a)
    #print('length of input: ' + str(length))
    size = 1
    numisl = float(raw_input().strip())
    if(numisl>1):
        maxlen = math.ceil((length/numisl)-1)
    else:
        maxlen = length

    runProcess()

if __name__ == '__main__':
    main()
    
'''
for s in subs.keys():
    cond = 0
    l = len(s)
    for i in xrange(length):
        
    for i in xrange(length):
        if(checkSubs() and cond==0):
            subs[s]+=1
            cond = -1
        else:
            cond = 0
        print(s + ":" + str(subs[s]))
        if(i+l>=length):
            if(subs[s]==numisl):
                finalcnt+=1
            break

print(str(finalcnt))
'''