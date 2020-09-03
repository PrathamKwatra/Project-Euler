#Project Euler Problem 3: Largest Prime Factor
#!/bin/python3

import sys
from math import sqrt
def prime_factorer(n):
    while (n%2==0):
        n=n/2
    if n==1:
        ans=2
        return ans
    i = 3
    while i <= sqrt(n):
        while n%i == 0:
            n = n/i
        i += 2

    if n>2:
        ans=n
        return (ans)
    else:
        ans=i-2
        return (ans)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n in range(10, (10**12)+1):
        ans = prime_factorer(n)
        print ('{:.0f}'.format(ans))
