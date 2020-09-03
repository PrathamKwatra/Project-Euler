#Project Euler Problem 6: Sum square Difference
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    limit = 1 + 10**4
    if n in range(1, limit):
        summation = (sum(range(1,n+1)))**2
        summation -= sum([((n**3)/3),(n**2/2),(n/6)])
        print ('{:.0f}'.format(summation))

