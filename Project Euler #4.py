#Project Euler Problem 4: Largest Palindrome Product
#!/bin/python3

import sys
pali = []
for i in range(100,1000):
    for j in range(100, 1000):
        a = (i*j)
        if a not in pali and (len(str(a))==6 and str(a) ==str(a)[::-1]):
            pali.append(a)
pali.sort()
leng = len(pali)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(leng-1, -1, -1):
        if pali[i]<n:
            print (pali[i])
            break
