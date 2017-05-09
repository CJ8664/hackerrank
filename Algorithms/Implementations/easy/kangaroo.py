# Problem URL https://www.hackerrank.com/challenges/kangaroo

def main():

    x1,v1,x2,v2 = raw_input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

    count = 1 
    n1=0
    n2=0
    
    if(x1 < x2 and v1 <= v2):
        print('NO')
    elif(x1 <= x2 and v1 < v2):
        print('NO')
    else:
        while(True):
            if(n1>n2):
                print('NO')
                break
            else:
                if(count==1):
                    n1 = x1 + v1
                    n2 = x2 + v2
                    count =0
                else:
                    n1 = n1 + v1
                    n2 = n2 + v2
                if(n1==n2):
                    print('YES')
                    break

if __name__ == '__main__':
    main()