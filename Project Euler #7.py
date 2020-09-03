#Project Euler Problem 7: 10001st Prime

import sys

def prime(n):
    arr = [True for i in range(n+1)]
    prime_list = []
    p = 2
    while (p * p <= n): 
        if (arr[p] == True): 
            for i in range(p * p, n+1, p): 
                arr[i] = False
        p += 1
    count = 0
    for i in range(2, n):
        if (arr[i]):
            prime_list.append(i)
    return prime_list    

prime_list = prime(104780)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (prime_list[n-1])
