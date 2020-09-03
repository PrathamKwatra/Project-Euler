#Project Euler Problem 2: Even Fibonacci Numbers
#!/bin/python3

import sys
def fibo(n):
    x = 1
    y = 1
    lst = []
    for i in range(n):
        if not x in range(n):
            break
        lst.append(x)
        y, x = x, (x+y)
#        print(y, x)
  #  print(lst)
    return lst

def even_fibo(n):
    n = n + 1
    arr = fibo(n)
    sum_arr = []
    for i in range(1, n, 3):
        try:
            if arr[i] in range(n):
                sum_arr.append(arr[i])
        except IndexError:
            break

   # print (sum_arr)
    return sum(sum_arr)

limit = 4*(10**16)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    constrains = [n in range(10,limit+1)]
    if all(constrains):
        sum_of_eve = even_fibo(n)
        print(sum_of_eve)
