a = input('a>> ')
b = input('b>> ')
c = input('c>> ')

if a > b:
    a,b =b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b    

print 'a = %d, b = %d, c = %d'%(a,b,c) 