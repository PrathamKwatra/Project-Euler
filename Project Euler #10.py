#Project Euler Problem 10: Summation of primes
#!/bin/python3

import sys

def prime(n):
    arr = [True for i in range(n+1)]
    prime_list = [2]
    p = 2
    while (p * p <= n): 
        if (arr[p] == True): 
            for i in range(p * p, n+1, p): 
                arr[i] = False
        p += 1
    for i in range(3, n, 2):
        if (arr[i]):
            prime_list.append(i)
    return prime_list


def fillPrefixSum(arr, n, prefixSum): 
  
    prefixSum[0] = arr[0] 
  
    # Adding present element 
    # with previous element 
    for i in range(1, n): 
        prefixSum[i] = prefixSum[i - 1] + arr[i] 

def b_search(n,h, start, stop):
    middle = 0
    while not stop < start:
        middle = start + (stop-start)//2
        if n==h[middle]:
            return middle
        if n < h[middle]:
            stop = middle - 1
        else:
            start = middle + 1
    return middle

length = 10**6
arr = prime(length+1)
n = len(arr)
prefixSum = [0]*(n+1)
fillPrefixSum(arr, n, prefixSum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i  = b_search(n,arr, 0, len(arr)-1)
    if (arr[i] > n):
        print(prefixSum[i-1])
    else:
        print (prefixSum[i])
