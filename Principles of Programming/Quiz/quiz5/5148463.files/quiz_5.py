# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
from copy import deepcopy
from collections import Counter


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    pass
    # Replace pass above with your code

# Insert your code for other functions
    
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

def expend_matrix(matrix):
    matrix.insert(0,list([0 for _ in range(width)]))
    matrix.append(list([0 for _ in range(width)]))
    for i in matrix:
        i.insert(0,0)
        i.append(0)
    return matrix


def recur_number(y,x):
    global temp_dict
    #print('This Time',y,x)
    if matrix[y][x]!=0:
        if matrix[y-1][x]-1==matrix[y][x]:
            temp_dict[(y,x,matrix[y][x])].append((y-1,x,matrix[y-1][x]))
        if matrix[y][x+1]-1==matrix[y][x]:
            temp_dict[(y,x,matrix[y][x])].append((y,x+1,matrix[y][x+1]))
        if matrix[y+1][x]-1==matrix[y][x]:
            temp_dict[(y,x,matrix[y][x])].append((y+1,x,matrix[y+1][x]))
        if matrix[y][x-1]-1==matrix[y][x]:
            temp_dict[(y,x,matrix[y][x])].append((y,x-1,matrix[y][x-1]))
        if matrix[y][x]==1:
            temp_dict[(y,x,matrix[y][x]-1)].append((y,x,matrix[y][x]))
            
def recur_check_dict(k):
    L=[]
    for v in temp_dict[k]:
        #print('All',v)
        x,y,z=v
        if v not in temp_dict.keys():
            final_list.append(z)
            #print('Z',z,v)
        else:
            L.append(v)
    for i in L:
        recur_check_dict(i)
    
        

#print('Before',grid)
matrix=deepcopy(grid)
expend_matrix(matrix)
#print('After',grid)
temp_dict=defaultdict(list)
#print('@@',grid)
for row_index,row in enumerate(grid):
    for line_index,line in enumerate(grid[row_index]):
        recur_number(row_index+1,line_index+1)
final_list=[]
        

        

for k in temp_dict.keys():
    x1,y1,z1=k
    if z1==1:
        #print('V',k)
        recur_check_dict(k)
    if (z1==0)&((x1,y1,z1+1) not in temp_dict.keys()):
        final_list.append(z1+1)
        #print('0',k)




paths = get_paths()
paths=Counter(final_list)  
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
