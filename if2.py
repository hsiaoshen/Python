a = input('a>> ')
b = input('b>> ')
c = input('c>> ')

if a > b:
    a,b =b,a
    if c < b:
        b,c = c,b
        if a > b:
            a,b = b,a
else:
    if b > c:
        b,c = c,b
        if a > b:
            a,b = b,a        
print 'a = %d, b = %d, c = %d'%(a,b,c)        