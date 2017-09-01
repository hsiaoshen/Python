import sys

a = sys.stdin.readline()

with open('file.txt','r+') as fd:
    for line in fd:
        if a == line:
            print 'exit'
            break
 