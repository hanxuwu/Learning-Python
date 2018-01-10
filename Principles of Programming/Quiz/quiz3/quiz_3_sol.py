# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    # A dictionary whose keys are step sizes, and whose values are dictionaries
    # whose keys are number of steps, and whose values are the number of stairs
    # of that many steps of that size.
    stairs = defaultdict(lambda : defaultdict(int))
    for step_size in range(2, (len(grid) + 1) // 2 + 1):
        for i in range(len(grid) - step_size + 1):
            for j in range(len(grid) - 2 * step_size + 2):
                nb_of_steps = step_down (i, j, step_size)
                if nb_of_steps:
                    stairs[step_size][nb_of_steps] += 1
    return {step_size: [(nb_of_steps, stairs[step_size][nb_of_steps])
                                                        for nb_of_steps in sorted(stairs[step_size])
                       ] for step_size in stairs
           }

def step_down(i, j, step_size):
    nb_of_steps = 0
    # ---
    i_0, j_0 = i, j
    for j in range(j, j + step_size):
        if not grid[i][j]:
            return 0
    if grid[i][j] == -step_size:
        return 0
    while i < len(grid) - step_size + 1 and j < len(grid) - step_size + 1:
        # |
        # |
        for i in range(i + 1, i + step_size):
            if not grid[i][j]:
                return nb_of_steps
        # ---
        for j in range(j + 1, j + step_size):
            if not grid[i][j]:
                return nb_of_steps
        grid[i][j] = -step_size
        nb_of_steps += 1
    return nb_of_steps

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
