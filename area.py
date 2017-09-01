
import math

a = int(input())
b = int(input())
c = int(input())

if a + b < c or a + c < b or b + c < a:
    print ("input error")

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print ('The area is %.2f'%area)