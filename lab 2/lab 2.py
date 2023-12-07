from math import *
from random import *
n=int(input("n="))
a=[0]*n
s=1
for i in range(n):
        a[i]= randint(-10,14)
print('A:',a)
for x in a:
    if x > 0:
        s*=x

print(s)