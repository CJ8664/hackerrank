#!/usr/local/bin/python

# Problem URL : https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(raw_input())
    my_list = list()
    for i in xrange(N):
        command = raw_input().strip().split(' ')
        cmd_type = command[0]
        params = [int(x) for x in command[1:]]
        
        if cmd_type == 'insert':
            my_list.insert(params[0], params[1])
        elif cmd_type == 'print':
            print(my_list)
        elif cmd_type == 'remove':
            my_list.remove(params[0])
        elif cmd_type == 'append':
            my_list.append(params[0])
        elif cmd_type == 'reverse':
            my_list.reverse()
        elif cmd_type == 'sort':
            my_list.sort()
        elif cmd_type == 'pop':
            my_list.pop()
