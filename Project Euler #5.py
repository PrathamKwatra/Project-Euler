#Project Euler Problem 5: Smallest Multiple
#!/bin/python3

import sys
def con_creator(n, i, constrain=[]):
    constrain.append(i%n==0)
    return constrain


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    q = True
    i = n
    while q:
        for num in range(2,n+1):
            constrain = con_creator(num, i)
            if not(constrain[-1]):
                break
        else:
            print(i)
            q = False
        i += n
