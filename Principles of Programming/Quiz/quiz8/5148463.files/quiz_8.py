# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


from collections import defaultdict
from copy import deepcopy
adjcent_matrix = defaultdict(list)


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
    pass
    # Replace pass above with your code
    
    



try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()


def expend_matrix(matrix):
    matrix.insert(0, list([-1 for _ in range(width)]))  # top of the matrix
    matrix.append(list([-1 for _ in range(width)]))  # bottom of the matrix
    for i in matrix:
        i.insert(0, -1)  # left od the matrix
        i.append(-1)  # right of the matrix
    return matrix

width=10
matrix = deepcopy(grid)
matrix = expend_matrix(matrix)
temp_dict = defaultdict(list)


def recur_number(y, x):  # generate the adjcent matrix
    global temp_dict
    # L_point=list(L)
    # print('This Time',y,x)
    if matrix[y - 1][x] != -1:  # north
        temp_dict[(y - 1, x - 1, matrix[y][x])
                  ].append((y - 1 - 1, x - 1, matrix[y - 1][x]))
    else:
        # pass
        temp_dict[(y - 1, x - 1, matrix[y][x])].append(None)
    if matrix[y][x + 1] != -1:  # east
        temp_dict[(y - 1, x - 1, matrix[y][x])
                  ].append((y - 1, x + 1 - 1, matrix[y][x + 1]))
    else:
        # pass
        temp_dict[(y - 1, x - 1, matrix[y][x])].append(None)
    if matrix[y + 1][x] != -1:  # south
        temp_dict[(y - 1, x - 1, matrix[y][x])
                  ].append((y + 1 - 1, x - 1, matrix[y + 1][x]))
    else:
        # pass
        temp_dict[(y - 1, x - 1, matrix[y][x])].append(None)
    if matrix[y][x - 1] != -1:  # left
        temp_dict[(y - 1, x - 1, matrix[y][x])
                  ].append((y - 1, x - 1 - 1, matrix[y][x - 1]))
    else:
        # pass
        temp_dict[(y - 1, x - 1, matrix[y][x])].append(None)


for row_index, row in enumerate(grid):
    for column_index, i in enumerate(grid[row_index]):
        # generate the adjcent matrix
        recur_number(column_index + 1, row_index + 1)
        # print(row_index,column_index)


sum = 0
flag_matrix = [[False for i in range(9)] for _ in range(9)]  # mark matrix
check_set = set()  # check if it is checked before
flag = False
final = []


def check_tempdict(y, x, target):
    global sum
    global flag_matrix
    global check_set
    global flag
    global final

    
    check_set.add((y, x))
    sum += grid[y][x]
    if sum>target:
        #print(f'There is no way to get a sum of {target} start from ({y},{x})')
        return
    final.append((y, x))
    for i in temp_dict[y, x, grid[y][x]]:  # find the first element

        if i:
            q, w, e = i
            if (q, w) not in check_set:
                new_y, new_x, new_i = i
                break
    if new_y == 0:  # end the initial state
        flag = True

    if not temp_dict[y, x, grid[y][x]][2]and flag:
        if temp_dict[y, x, grid[y][x]][3]:  # the bottom one move to the left
            new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][3]
    number_checked = 0
    for i in temp_dict[y, x, grid[y][x]][1:3]:  # right bottom  corner

        if i:
            q, w, e = i
            if (q, w) in check_set:
                number_checked += 1

    
    if number_checked == 2:
        new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][3]
        number_checked = 0

    if sum + new_i < target:
        if (new_y, new_x) not in check_set:
            return check_tempdict(new_y, new_x, target)
        else:
            if temp_dict[y, x, grid[y][x]][0]:
                new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][0]
                if (new_y, new_x) not in check_set:
                    return check_tempdict(new_y, new_x, target)
            if temp_dict[y, x, grid[y][x]][1]:
                new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][1]
                if (new_y, new_x) not in check_set:
                    return check_tempdict(new_y, new_x, target)
            if temp_dict[y, x, grid[y][x]][2]:
                new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][2]
                if (new_y, new_x) not in check_set:
                    return check_tempdict(new_y, new_x, target)
            if temp_dict[y, x, grid[y][x]][3]:
                new_y, new_x, new_i = temp_dict[y, x, grid[y][x]][3]
                if (new_y, new_x) not in check_set:
                    return check_tempdict(new_y, new_x, target)
    if sum + new_i == target:
        final.append((new_y, new_x))
    if sum + new_i > target:

        for i in temp_dict[y, x, grid[y][x]][1:]:
            if i:
                a, b, c = i
                if sum + c == target:
                    final.append((a, b))
                    break
                q, w, e = i
                if (q, w) not in check_set:
                    new_y, new_x, new_i = i
                    if sum + new_i <= target:
                        return check_tempdict(new_y, new_x, target)
            else:
                return check_tempdict(new_y, new_x, target)[3]

#print(y,x,target)            
check_tempdict(x, y, target)
#print(len(final))
#check_tempdict(9, 5, 11)

path = final

if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
