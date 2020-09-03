#Project Euler Problem 9: Special Pythagorean Triplet
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    num = int(input().strip())
    maximum_product = -1
    for a in range(1,num//2):
        b = (((num**2)/2) - (num*a)) // (num - a)
        if b > 0:
            hyp = (a**2 + b**2)**0.5
            if a + b + hyp == num:
                prod = a*b*hyp
                if maximum_product < prod:
                    maximum_product = prod
    print(int(maximum_product))
