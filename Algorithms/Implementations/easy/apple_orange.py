# Problem URL https://www.hackerrank.com/challenges/apple-and-orange

def main():

    house_left, house_right = raw_input().strip().split(' ')
    apple, orange = raw_input().strip().split(' ')
    napp, norg = raw_input().strip().split(' ')
    
    house_left = int(house_left)
    house_right = int(house_right)
    apple = int(apple)
    orange = int(orange)
    napp = int(napp)
    norg = int(norg)
    
    count = 0
    for dist in raw_input().strip().split(' '): # Apples
        dist = int(dist)
        #print(str(apple + dist))
        if((apple + dist) >= house_left and (apple + dist) <= house_right):
            count+= 1
    print(str(count))
    
    count = 0
    for dist in raw_input().strip().split(' '): # Oranges
        dist = int(dist)
        #print(str(orange + dist))
        if((orange + dist) <= house_right and (orange + dist) >= house_left):
            count+= 1
    print(str(count))
    
if __name__ == '__main__':
    main()