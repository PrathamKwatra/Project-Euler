#Project Euler Problem 11: Largest Product in a Grid
#!/bin/python3

import sys

def prod(num):
    return num[0] * num[1] * num [2] * num[3]

grid = []
max_side = 0
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
#Side_Way
    side_ways = [prod([grid_t[i], grid_t[i+1], grid_t[i+2], grid_t[i+3]]) for i in range(17)]
    if max(side_ways) > max_side:
        max_side = max(side_ways)
#Down
max_down = 0
for i in range(20):
    down_motion = [prod([grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]) for j in range(17)]
    if max_down < max(down_motion):
        max_down = max(down_motion)
#Diagnol
max_diag = 0
for i in range(17):
    normal_diag = [prod([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]) for j in range(17)]
    reverse_diag = [prod([grid[i][19-j], grid[i+1][18-j], grid[i+2][17-j], grid[i+3][16-j]]) for j in range(17)]
    if max(normal_diag) > max(reverse_diag):
        max_diag = max(normal_diag) if max(normal_diag) > max_diag else max_diag
    else:
        max_diag = max(reverse_diag) if max(reverse_diag) > max_diag else max_diag 
final_sum = [max_down, max_side, max_diag]
print (max(final_sum))
