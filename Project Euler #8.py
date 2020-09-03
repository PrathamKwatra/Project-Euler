#Project Euler Problem 8: Largest Product in a Series
from operator import mul
import sys
from functools import reduce

def result(max_num):
    maximum_result = 1
    for i in max_num:
        maximum_result *= int(i)
    return (maximum_result)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    new_num = []
    while len(str(num)) != k:
        new_num.append((str(num)[:k]))
        num = str(num)[1:]
    for i in range(len(new_num)):
        new_num[i] = result(new_num[i])
    print(max(new_num))
