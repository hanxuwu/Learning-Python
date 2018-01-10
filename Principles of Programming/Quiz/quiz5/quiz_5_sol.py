# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    paths = defaultdict(int)
    for i in range(height):
        for j in range(width):
            if grid[i][j] != 1:
                continue
            extend(paths, 1, i, j)
    return paths

def get_paths_from(n, i, j):
    if i < 0 or i >= height or j < 0 or j >= width:
        return
    if grid[i][j] != n:
           return
    paths = defaultdict(int)
    for a, b in {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}:
        extend(paths, n + 1, a, b)
    if not paths:
        paths = {n: 1}
    return paths

def extend(paths, n, i, j):
    extensions = get_paths_from(n, i, j)
    if extensions:
        for length in extensions:
            paths[length] += extensions[length]
    return paths
    
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
