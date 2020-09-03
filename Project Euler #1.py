#Project Euler Problem 1: Multiples of 3 and 5
#!/bin/python3

import sys, math
def multiple(num):
    ##multiple of 3
    n = num//3
    if not(num%3 == 0):
        sum_of_3 = (n)*((2*3) + (n-1)*3)
    else:
        n -= 1
        sum_of_3 = (n)*((2*3) + (n-1)*3)
    ##multiple of 5
    n = num//5
    if not(num%5 == 0):
        sum_of_5 = (n)*((2*5) + (n-1)*5)
    else:
        n -= 1
        sum_of_5 = (n)*((2*5) + (n-1)*5)
    ##multiple of 15
    n = num//15
    if not(num%15 == 0):
        sum_of_15 = (n)*((2*15) + (n-1)*15)
    else:
        n -= 1
        sum_of_15 = (n)*((2*15) + (n-1)*15)
    total = sum_of_3 + sum_of_5 - sum_of_15
    return (total//2)
t = int(input().strip())
limit_t = 10**5
limit_n = 10**9
if t in range(1, limit_t+1):
    for a0 in range(t):
        n = int(input().strip())
        if n in range(1, limit_n +1):
            n_factors = multiple(n)
         ##   print ('{:.0f}'.format(n_factors))
            print((n_factors))
        
