
# This file is just for testing some simple code
#%%
# check the current location
import os
print(os.getcwd())
# change the current location
os.chdir("C:\Study\VScode\Assignment\Assignment2")
print(os.getcwd())

#%%
# check the missing line
import os
print(os.getcwd())
sudoku_list = []
with open("sudoku_wrong_2.txt", encoding='utf-8') as original_grid:  # open the file
    for digit in original_grid:
        sudoku_list.append(digit.split())  # separate by split

for i in sudoku_list:
    print(i)


#%%
# pythonic the language
class SudokuError(Exception):  # Create the SudokuError class to check the input
    def __init__(self, message):
        self.message = message


class Sudoku(object):  # Sudoku class
    def __init__(self, *args):
        self.filename = args   # filename
        self.sudoku_list = []  # to store the filestream
        print(args)

        with open(*args, encoding='utf-8') as original_grid:  # open the file
            for digit in original_grid:
                self.sudoku_list.append(digit.split())  # separate by split
            print(self.sudoku_list)

        L = []  # store the number
        for digit_string in self.sudoku_list:
            for i in digit_string:
                try:
                    L.append(int(i))  # problem if i is letter
                except:
                    raise SudokuError('Incorrect input')

        n = 9
        # split the list to sub list len of n
        matrix = tuple(L[i:i + n] for i in range(0, len(L), n))

        print(L)
        print(len(L))  # check the number of the list
        print(matrix)

        if(len(L)) != 81:
            raise SudokuError('Incorrect input')


Sudoku('sudoku_wrong_1.txt')

#%%
# check the solvable
matrix = ([0, 0, 1, 9, 0, 0, 0, 0, 8],
          [6, 0, 0, 0, 8, 5, 0, 3, 0],
          [0, 0, 7, 0, 6, 0, 1, 0, 0],
          [0, 3, 4, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 2, 0],
          [0, 0, 5, 0, 7, 0, 9, 0, 0],
          [0, 1, 0, 8, 6, 0, 0, 0, 7],
          [7, 0, 0, 0, 0, 9, 2, 0, 0])

# original matrix
list_matrix = list(matrix)
for row in list_matrix:
    print(row)
print()

# convert the matrix row<--->column
convert_list_matrix = list(map(list, zip(*list_matrix)))
for row in convert_list_matrix:
    print(row)
print()

# grab the subbox
# index the matrix

subbox_list = []
for row_index, row in enumerate(list_matrix):
    for line_index, i in enumerate(row):
        print(row_index + 1, line_index + 1, i)
print(new_matrix)
print(subbox_list)

#%%
# Modify the matrix
from collections import defaultdict
sudoku_list = [0, 0, 1, 9, 0, 0, 0, 0, 8, 6, 0, 0, 0, 8, 5, 0, 3, 0, 0, 0, 7, 0, 6, 0, 1, 0, 0, 0, 3, 4, 0, 9, 0, 0, 0, 0, 0, 0,
               0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 2, 0, 0, 0, 5, 0, 7, 0, 9, 0, 0, 0, 1, 0, 8, 6, 0, 0, 0, 7, 7, 0, 0, 0, 0, 9, 2, 0, 0]
n = 3
matrix = list(sudoku_list[i:i + n] for i in range(0, len(sudoku_list), n))
print(matrix)
n = 3
matrix1 = list(matrix[i:i + n] for i in range(0, len(matrix), n))
print(matrix1)
subbox_list = zip(matrix1)
for i in subbox_list:
    print(i)

#%%
matrix = ([0, 0, 1, 9, 0, 0, 0, 0, 8],
          [6, 0, 0, 0, 8, 5, 0, 3, 0],
          [0, 0, 7, 0, 6, 0, 1, 0, 0],
          [0, 3, 4, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 2, 0],
          [0, 0, 5, 0, 7, 0, 9, 0, 0],
          [0, 1, 0, 8, 6, 0, 0, 0, 7],
          [7, 0, 0, 0, 0, 9, 2, 0, 0])
L1 = []
print(matrix)
for row in matrix:
    n = 3
    L.append(list(row[i:i + n] for i in range(0, len(row), n)))
zip_matrix = (list(zip(*L)))
L2 = []
for row in zip_matrix:
    n = 3
    L2.append(list(row[i:i + n] for i in range(0, len(row), n)))

print('L2')
print(L2)

print('For L2')
for i in L2:
    print(i)

print('unpack')
print(*zip(*L2))

#%%
# silly solution to get the subbox
matrix = ([0, 0, 1, 9, 0, 0, 0, 0, 8],
          [6, 0, 0, 0, 8, 5, 0, 3, 0],
          [0, 0, 7, 0, 6, 0, 1, 0, 0],
          [0, 3, 4, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 2, 0],
          [0, 0, 5, 0, 7, 0, 9, 0, 0],
          [0, 1, 0, 8, 6, 0, 0, 0, 7],
          [7, 0, 0, 0, 0, 9, 2, 0, 0])
print(matrix)
from collections import defaultdict
subbox = defaultdict(list)
for index_row, row in enumerate(matrix):
    for index_column, i in enumerate(row):
        print(index_row, index_column, i)

        if index_row // 3 == 0 and index_column // 3 == 0:
            subbox[1].append(i)
        if index_row // 3 == 0 and index_column // 3 == 1:
            subbox[2].append(i)
        if index_row // 3 == 0 and index_column // 3 == 2:
            subbox[3].append(i)
        if index_row // 3 == 1 and index_column // 3 == 0:
            subbox[4].append(i)
        if index_row // 3 == 1 and index_column // 3 == 1:
            subbox[5].append(i)
        if index_row // 3 == 1 and index_column // 3 == 2:
            subbox[6].append(i)
        if index_row // 3 == 2 and index_column // 3 == 0:
            subbox[7].append(i)
        if index_row // 3 == 2 and index_column // 3 == 1:
            subbox[8].append(i)
        if index_row // 3 == 2 and index_column // 3 == 2:
            subbox[9].append(i)
print(subbox)


#%%
# print the subbox of the sudoku
matrix = ([0, 0, 1, 9, 0, 0, 0, 0, 8],
          [6, 0, 0, 0, 8, 5, 0, 3, 0],
          [0, 0, 7, 0, 6, 0, 1, 0, 0],
          [0, 3, 4, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 2, 0],
          [0, 0, 5, 0, 7, 0, 9, 0, 0],
          [0, 1, 0, 8, 6, 0, 0, 0, 7],
          [7, 0, 0, 0, 0, 9, 2, 0, 0])
from collections import defaultdict
subbox = defaultdict(list)
for row_index, row in enumerate(matrix):
    for column_index, i in enumerate(row):
        print(row_index, column_index, i)
        subbox[row_index // 3 * 3 + column_index // 3].append(i)
for i in subbox.values():
    print(i)


#%%
# try to pythonic
matrix = ([0, 0, 1, 9, 0, 0, 0, 0, 8],
          [6, 0, 0, 0, 8, 5, 0, 3, 0],
          [0, 0, 7, 0, 6, 0, 1, 0, 0],
          [0, 3, 4, 0, 9, 0, 0, 0, 0],
          [0, 0, 0, 5, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 4, 2, 0],
          [0, 0, 5, 0, 7, 0, 9, 0, 0],
          [0, 1, 0, 8, 6, 0, 0, 0, 7],
          [7, 0, 0, 0, 0, 9, 2, 0, 0])
# row
print(list(matrix))
matrix_row = list(matrix)
# column
matrix_column = list(map(list, zip(*matrix)))
print(matrix_column)

# subbox
merged_matrix = sum(matrix, [])
print(merged_matrix)
tri_matrix = [merged_matrix[i:i + 3] for i in range(0, len(merged_matrix), 3)]
print(tri_matrix)
#subbox=[tri_matrix[i:i+9:3]for a in range(0,9,3)  for i in range(a,a+3) ]
# range(0,3)
#[[0, 0, 1], [6, 0, 0], [0, 0, 7]]
#[[9, 0, 0], [0, 8, 5], [0, 6, 0]]
#[[0, 0, 8], [0, 3, 0], [1, 0, 0]]

# range(9,12)
#[[0, 3, 4], [0, 0, 0], [0, 0, 0]]
#[[0, 9, 0], [5, 0, 4], [0, 1, 0]]
#[[0, 0, 0], [0, 0, 0], [4, 2, 0]]

# range(18,21)
#[[0, 0, 5], [0, 1, 0], [7, 0, 0]]
#[[0, 7, 0], [8, 6, 0], [0, 0, 9]]
#[[9, 0, 0], [0, 0, 7], [2, 0, 0]]

subbox = [sum(tri_matrix[i:i + 9:3], [])
          for a in (0, 9, 18)for i in range(a, a + 3)]
print(subbox)

for i in subbox:
    print(i)

#%%
# check the valid

for a in matrix_row:
    check_list = []
    for i in a:
        if i == 0:
            continue
        else:
            check_list.append(i)
    print('A', check_list)
    if len(check_list) != len(set(check_list)):
        print('IMPOSSIBLE')
for b in matrix_column:
    check_list = []
    for i in b:
        if i == 0:
            continue
        else:
            check_list.append(i)
    print('B', check_list)
    if len(check_list) != len(set(check_list)):
        print('IMPOSSIBLE')

check_list = []
for c in subbox:
    check_list = []
    for i in c:
        if i == 0:
            continue
        else:
            check_list.append(i)
    print('C', check_list)
    if len(check_list) != len(set(check_list)):
        print('IMPOSSIBLE')


#%%
# build the matrix dict,include all the situation
from collections import defaultdict
from copy import deepcopy

sudoku_dict = dict()  # convert the sudoku to a dict
box = dict()  # each subbox
for y in range(9):
    for x in range(9):
        for i in range(5):
            box[i] = dict()
        sudoku_dict[(y, x)] = deepcopy(box)
sudoku_dict

# position(0,1) upper left corner add the possible solution 1,the mark is True
sudoku_dict[0, 1][0][1] = True
sudoku_dict[0, 1][4] = 5  # position(0,1) middle one assign the number 5
sudoku_dict


#%%
# change to the dict:dict,{middle}
from collections import defaultdict
from copy import deepcopy

sudoku_dict = dict()
box = dict()
for y in range(9):
    for x in range(9):
        for i in range(1, 11):
            box[i] = None  # None  True：mark  False：exist
        sudoku_dict[(y, x)] = deepcopy(box)
sudoku_dict

sudo3 = [[0, 0, 1, 9, 0, 0, 0, 0, 8],
         [6, 0, 0, 0, 8, 5, 0, 3, 0],
         [0, 0, 7, 0, 6, 0, 1, 0, 0],
         [0, 3, 4, 0, 9, 0, 0, 0, 0],
         [0, 0, 0, 5, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 4, 2, 0],
         [0, 0, 5, 0, 7, 0, 9, 0, 0],
         [0, 1, 0, 8, 4, 0, 0, 0, 7],
         [7, 0, 0, 0, 0, 9, 2, 0, 0]]

for row_index, row in enumerate(sudo3):
    for column_index, i in enumerate(row):
        # print(row_index,column_index,i)
        if i != 0:
            sudoku_dict[row_index, column_index][10] = i
sudoku_dict


# generate the  tex from a dictionary
def generate_tex():
    sudoku_string = []
    for line in range(0, 9):  # row
        sudoku_string.append('\n')
        sudoku_string.append('% Line ' + f'{line+1}' + '\n')
        for col in range(0, 9):
            middle_digit = None
            upper_left_corner = []
            temp_dict = dict()
            upper_left_corner = ''
            upper_right_corner = ''
            lower_left_corner = ''
            lower_right_corner = ''
            if sudoku_dict[line, col][10]:  # if the middle number has been decided
                middle_digit = sudoku_dict[line, col][10]

            # if the middle number has been decided
            for k, v in sorted(sudoku_dict[line, col].items()):
                if v == True and k <= 9:  # cancel one
                    temp_dict[k] = '\\cancal' + '{' + str(k) + '}'
                if v == False and k <= 9:  # kept one
                    temp_dict[k] = str(k)

            for k, v in sorted(temp_dict.items()):
                if k in range(1, 3):
                    upper_left_corner = ' ' + temp_dict[k]
                if k in range(3, 5):
                    upper_right_corner = ' ' + temp_dict[k]
                if k in range(5, 7):
                    lower_left_corner = ' ' + temp_dict[k]
                if k in range(7, 10):
                    lower_right_corner += ' ' + temp_dict[k]

            sudoku_string.append('\\N')
            if upper_left_corner:
                sudoku_string.append('{'f'{upper_left_corner.strip()}''}')
            else:
                sudoku_string.append('{}')  # upper left corner
            if upper_right_corner:
                sudoku_string.append('{'f'{upper_right_corner.strip()}''}')
            else:
                sudoku_string.append('{}')  # upper right corner
            if lower_left_corner:
                sudoku_string.append('{'f'{lower_left_corner.strip()}''}')
            else:
                sudoku_string.append('{}')  # lower left corner
            if lower_right_corner:
                sudoku_string.append('{'f'{lower_right_corner.strip()}''}')
            else:
                sudoku_string.append('{}')  # lower right corner
            if middle_digit:  # out put the middle number
                sudoku_string.append('{'f'{middle_digit}''}')
            else:
                sudoku_string.append('{}')
            if col in (0, 1, 3, 4, 6, 7):
                sudoku_string.append(' & ')
            if col in (2, 5):
                sudoku_string.append(' &')  # at the end don't need the space
                sudoku_string.append('\n')
        if line in (2, 5):  # print(double line)
            sudoku_string.append(" \\\ \hline\hline")
            sudoku_string.append('\n')
        if line == 8:  # print(double line)
            sudoku_string.append(" \\\ \hline\hline")
        if line in (0, 1, 3, 4, 6, 7):
            sudoku_string.append(" \\\ \hline")
            sudoku_string.append('\n')
    return sudoku_string


sudoku_comment = generate_tex()
sudoku_comment = ''.join(sudoku_comment)
print(sudoku_comment)


import os
print(os.getcwd())
os.chdir('C:\Study\VScode\Assignment\Assignment2')
# initial comment
initial_comment = r"""\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline"""

# finalize comment
finalize_comment = r"""
\end{tabular}
\end{center}

\end{document}
"""
# function output the tex


def tex_output(string_list):
    initial = []

    def initialize():
        initial.append(initial_comment)

    def add_sudoku():
        initial.append(string_list)

    def finalize():
        initial.append(finalize_comment)
    initialize()
    add_sudoku()
    finalize()
    initial = "".join(initial)
    file_name = 'TestTexOutput' + '.tex'
    with open(file_name, 'w') as f:
        f.write(initial)


tex_output(sudoku_comment)


#%% find the forced number TODO: THIS VERSION ONLY CHECK ONCE
from collections import defaultdict
from copy import deepcopy
from collections import Counter

matrix_row = [[0, 0, 1, 9, 0, 0, 0, 0, 8],
              [6, 0, 0, 0, 8, 5, 0, 3, 0],
              [0, 0, 7, 0, 6, 0, 1, 0, 0],
              [0, 3, 4, 0, 9, 0, 0, 0, 0],
              [0, 0, 0, 5, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 4, 2, 0],
              [0, 0, 5, 0, 7, 0, 9, 0, 0],
              [0, 1, 0, 8, 4, 0, 0, 0, 7],
              [7, 0, 0, 0, 0, 9, 2, 0, 0]]
matrix_column = [[0, 6, 0, 0, 0, 0, 0, 0, 7],
                 [0, 0, 0, 3, 0, 0, 0, 1, 0],
                 [1, 0, 7, 4, 0, 0, 5, 0, 0],
                 [9, 0, 0, 0, 5, 0, 0, 8, 0],
                 [0, 8, 6, 9, 0, 1, 7, 4, 0],
                 [0, 5, 0, 0, 4, 0, 0, 0, 9],
                 [0, 0, 1, 0, 0, 4, 9, 0, 2],
                 [0, 3, 0, 0, 0, 2, 0, 0, 0],
                 [8, 0, 0, 0, 0, 0, 0, 7, 0]]
subbox = [[0, 0, 1, 6, 0, 0, 0, 0, 7],
          [9, 0, 0, 0, 8, 5, 0, 6, 0],
          [0, 0, 8, 0, 3, 0, 1, 0, 0],
          [0, 3, 4, 0, 0, 0, 0, 0, 0],
          [0, 9, 0, 5, 0, 4, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 4, 2, 0],
          [0, 0, 5, 0, 1, 0, 7, 0, 0],
          [0, 7, 0, 8, 4, 0, 0, 0, 9],
          [9, 0, 0, 0, 0, 7, 2, 0, 0]]

sudoku_dict = dict()
box = dict()  # each small box
for y in range(9):
    for x in range(9):
        for i in range(1, 11):  # 1-9 is the number in the corner,10 is the middle number
            box[i] = None  # None  True：mark  False：exist
        # deepcopy the  box otherwise if one change all change
        sudoku_dict[(y, x)] = deepcopy(box)

# generate the bare sudo dictionary
for row_index, row in enumerate(matrix_row):
    for column_index, i in enumerate(row):
        # print(row_index,column_index,i)
        if i != 0:
            sudoku_dict[row_index, column_index][10] = i
        print(row_index, column_index, sudoku_dict[row_index, column_index])

# DONE TODO: FROM LOCATION TO SUBBOX INDEX,
# generate a dict that contain the location of each subbox
subbox_index_location = defaultdict(list)  # subindex to location
subbox_location_index = dict()  # location to subindex
# DONE TODO: FROM ROW INDEX TO LOCATION
row_index_location = defaultdict(list)  # row index to location
column_index_location = defaultdict(list)  # row index to location

for y in range(9):
    for x in range(9):
        subbox_index_location[y // 3 * 3 + x //
                              3].append((y, x))  # add location to subindex
        subbox_location_index[(y, x)] = y // 3 * 3 + \
            x // 3  # add subindex to location
        row_index_location[y].append((y, x))  # add location to row_index
        column_index_location[x].append((y, x))  # add location to column_index
subbox_index_location  # 0:(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)......
subbox_location_index  # (0, 8): 2
print('@', row_index_location)
print('#', column_index_location)


# TODO: DO NOT CHECK THE GIVEN BOX
row_index_location = defaultdict(list)  # initial the row_index_location
column_index_location = defaultdict(list)  # initial the column_location
subbox_index_location = defaultdict(list)

possible_dict = dict()
for y in range(9):
    for x in range(9):
        temp_set = set()  # temporary set to find exist number
        flag = False
        if matrix_row[y][x] != 0:
            flag = True  # mark the given digit
        for mr in matrix_row[y]:  # check if the number in row
            if mr != 0:
                temp_set.add(mr)
        for mc in matrix_column[x]:  # check if the number in column
            if mc != 0:
                temp_set.add(mc)
        # TODO:FROM LOCATION TO SUBBOX INDEX #check if the number in subbox
        for sb in subbox[subbox_location_index[y, x]]:
            if sb != 0:
                temp_set.add(sb)
        print(y, x, temp_set)
        if flag:  # check if the number has been given
            continue
        possible_dict[y, x] = set(range(1, 10)) - temp_set
        # TODO: DO NOT CHECK THE GIVEN BOX
        row_index_location[y].append((y, x))
        # TODO: DO NOT CHECK THE GIVEN BOX
        column_index_location[x].append((y, x))
        # TODO: DO NOT CHECK THE GIVEN BOX
        subbox_index_location[y // 3 * 3 + x // 3].append((y, x))
# possible_dict
# TODO: generate the dict index of each line and each row in order to force check in the sudoku_dict

# use possible_dict check the force sudomateix

test_matrix_row = [[0, 0, 1, 9, 0, 0, 0, 0, 8],
                   [6, 0, 0, 0, 8, 5, 0, 3, 0],
                   [0, 0, 7, 0, 6, 0, 1, 0, 0],
                   [0, 3, 4, 0, 9, 0, 0, 0, 0],
                   [0, 0, 0, 5, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 4, 2, 0],
                   [0, 0, 5, 0, 7, 0, 9, 0, 0],
                   [0, 1, 0, 8, 4, 0, 0, 0, 7],
                   [7, 0, 0, 0, 0, 9, 2, 0, 0]]

for k, v in possible_dict.items():
    if len(v) == 1:  # find the definately digit.
        print('☝', k, v)
        a, b = k  # unpack the location
        subbox_index = subbox_location_index[k]  # get the sub index
        for i in v:
            value = i  # get the number in set
        test_matrix_row[a][b] = int(str(*v))
        for i in row_index_location[a]:
            if value in possible_dict[i]:  # update the row
                print('🍣', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(value)
        for i in column_index_location[b]:
            if value in possible_dict[i]:  # update the column
                print('🍚', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(value)
        for i in subbox_index_location[subbox_index]:
            if value in possible_dict[i]:  # update the subbox
                print('🍕', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(value)


updatedict = dict()  # date need to be update
for i in range(9):  # check the row、column and subbox
    row_list = list()
    c_row = Counter()

    column_list = list()
    c_column = Counter()

    subbox_list = list()
    c_subbox = Counter()
    # check the possible number row by row except the given number
    for row_location in row_index_location[i]:
        print(row_location)
        row_list += list(possible_dict[row_location])
    # print('@',row_list)
    c_row = Counter(row_list)
    print(c_row)
    for k1, v1 in c_row.items():
        if v1 == 1:
            print('🍐', k1)
            for row_location in row_index_location[i]:
                if k1 in possible_dict[row_location]:
                    print('⌛', row_location)  # find the only one in row
                    updatedict[row_location] = k1

    # check the possible number column by row except the given number
    for column_location in column_index_location[i]:
        print(column_location)
        column_list += list(possible_dict[column_location])
    # print('@',row_list)
    c_column = Counter(column_list)
    print(c_column)
    for k2, v2 in c_column.items():
        if v2 == 1:
            print('🍏', k2)
            for column_location in column_index_location[i]:
                if k2 in possible_dict[column_location]:
                    print('⌛', column_location)  # find the only one in column
                    updatedict[column_location] = k2

    # check the possible number column by row except the given number
    for subbox_location in subbox_index_location[i]:
        print(subbox_location)
        subbox_list += list(possible_dict[subbox_location])
    # print('@',row_list)
    c_subbox = Counter(subbox_list)
    print(c_column)
    for k3, v3 in c_subbox.items():
        if v3 == 1:
            print('🍓', k3)
            for subbox_location in subbox_index_location[i]:
                if k3 in possible_dict[subbox_location]:
                    print('⌛', subbox_location)  # find the only one in subbox
                    updatedict[subbox_location] = k3

print(updatedict)  # TODO: DELETE THE FINAL ONE
# update the possible_dict
for k1, v1 in updatedict.items():  # update the possible_dict first
    # for k2,v2 in possible_dict.items():
    y, x = k1
    test_matrix_row[y][x] = v1
    possible_dict[k1] = set()  # delete the found number
    # update the line row and subbox
    subbox_index = subbox_location_index[k1]  # get the sub index
    for i in row_index_location[y]:
        if v1 in possible_dict[i]:  # update the row
            print('🍣', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)
    for i in column_index_location[x]:
        if v1 in possible_dict[i]:  # update the column
            print('🍚', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)
    for i in subbox_index_location[subbox_index]:
        if v1 in possible_dict[i]:  # update the subbox
            print('🍕', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)


print(possible_dict)
print(test_matrix_row)
possible_dict
# test_matrix_row


# TODO:Extract the function AND Find all the forced number
#%% find the forced number
from collections import defaultdict
from copy import deepcopy
from collections import Counter

matrix_row = [[0, 0, 1, 9, 0, 0, 0, 0, 8],
              [6, 0, 0, 0, 8, 5, 0, 3, 0],
              [0, 0, 7, 0, 6, 0, 1, 0, 0],
              [0, 3, 4, 0, 9, 0, 0, 0, 0],
              [0, 0, 0, 5, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 4, 2, 0],
              [0, 0, 5, 0, 7, 0, 9, 0, 0],
              [0, 1, 0, 8, 4, 0, 0, 0, 7],
              [7, 0, 0, 0, 0, 9, 2, 0, 0]]
matrix_column = [[0, 6, 0, 0, 0, 0, 0, 0, 7],
                 [0, 0, 0, 3, 0, 0, 0, 1, 0],
                 [1, 0, 7, 4, 0, 0, 5, 0, 0],
                 [9, 0, 0, 0, 5, 0, 0, 8, 0],
                 [0, 8, 6, 9, 0, 1, 7, 4, 0],
                 [0, 5, 0, 0, 4, 0, 0, 0, 9],
                 [0, 0, 1, 0, 0, 4, 9, 0, 2],
                 [0, 3, 0, 0, 0, 2, 0, 0, 0],
                 [8, 0, 0, 0, 0, 0, 0, 7, 0]]
subbox = [[0, 0, 1, 6, 0, 0, 0, 0, 7],
          [9, 0, 0, 0, 8, 5, 0, 6, 0],
          [0, 0, 8, 0, 3, 0, 1, 0, 0],
          [0, 3, 4, 0, 0, 0, 0, 0, 0],
          [0, 9, 0, 5, 0, 4, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 4, 2, 0],
          [0, 0, 5, 0, 1, 0, 7, 0, 0],
          [0, 7, 0, 8, 4, 0, 0, 0, 9],
          [9, 0, 0, 0, 0, 7, 2, 0, 0]]

sudoku_dict = dict()
box = dict()  # each small box
for y in range(9):
    for x in range(9):
        for i in range(1, 11):  # 1-9 is the number in the corner,10 is the middle number
            box[i] = None  # None  True：mark  False：exist
        # deepcopy the  box otherwise if one change all change
        sudoku_dict[(y, x)] = deepcopy(box)

# generate the bare sudo dictionary
for row_index, row in enumerate(matrix_row):
    for column_index, i in enumerate(row):
        # print(row_index,column_index,i)
        if i != 0:
            sudoku_dict[row_index, column_index][10] = i
        print(row_index, column_index, sudoku_dict[row_index, column_index])

# generate the subbox_index for check if number in subbox
# generate a dict that contain the location of each subbox
subbox_location_index = dict()  # location to subindex
for y in range(9):
    for x in range(9):
        subbox_location_index[(y, x)] = y // 3 * 3 + \
            x // 3  # add subindex to location
subbox_location_index  # (0, 8): 2
print('@', row_index_location)
print('#', column_index_location)


# TODO: DO NOT CHECK THE GIVEN BOX
# DONE TODO: FROM ROW INDEX TO LOCATION
row_index_location = defaultdict(list)  # initial the row_index_location
column_index_location = defaultdict(list)  # initial the column_location
# 0:(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)......
subbox_index_location = defaultdict(list)

possible_dict = dict()
for y in range(9):
    for x in range(9):
        temp_set = set()  # temporary set to find exist number
        flag = False  # check if the number has been given
        if matrix_row[y][x] != 0:
            flag = True  # mark the given digit
        for mr in matrix_row[y]:  # check if the number in row
            if mr != 0:
                temp_set.add(mr)
        for mc in matrix_column[x]:  # check if the number in column
            if mc != 0:
                temp_set.add(mc)
        # TODO:FROM LOCATION TO SUBBOX INDEX #check if the number in subbox
        for sb in subbox[subbox_location_index[y, x]]:
            if sb != 0:
                temp_set.add(sb)
        print(y, x, temp_set)
        if flag:  # check if the number has been given
            continue
        possible_dict[y, x] = set(range(1, 10)) - temp_set
        # DO NOT CHECK THE GIVEN BOX
        row_index_location[y].append((y, x))  # add location to row_index
        column_index_location[x].append((y, x))  # add location to column_index
        subbox_index_location[y // 3 * 3 + x //
                              3].append((y, x))  # add location to subindex
# possible_dict
# TODO: generate the dict index of each line and each row in order to force check in the sudoku_dict

# use possible_dict check the force sudomateix

test_matrix_row = [[0, 0, 1, 9, 0, 0, 0, 0, 8],
                   [6, 0, 0, 0, 8, 5, 0, 3, 0],
                   [0, 0, 7, 0, 6, 0, 1, 0, 0],
                   [0, 3, 4, 0, 9, 0, 0, 0, 0],
                   [0, 0, 0, 5, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 4, 2, 0],
                   [0, 0, 5, 0, 7, 0, 9, 0, 0],
                   [0, 1, 0, 8, 4, 0, 0, 0, 7],
                   [7, 0, 0, 0, 0, 9, 2, 0, 0]]


def update_possible_dict(k1, v1):
    y, x = k1
    test_matrix_row[y][x] = v1
    sudoku_dict[k1][10] = v1  # update the out_put latex dict
    possible_dict[k1] = set()  # delete the found number
    # update the line row and subbox
    subbox_index = subbox_location_index[k1]  # get the sub index
    for i in row_index_location[y]:
        if v1 in possible_dict[i]:  # update the row
            print('🍣', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)
    for i in column_index_location[x]:
        if v1 in possible_dict[i]:  # update the column
            print('🍚', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)
    for i in subbox_index_location[subbox_index]:
        if v1 in possible_dict[i]:  # update the subbox
            print('🍕', i)
            # possible_dict[i]-{int(str(*v))}
            possible_dict[i].remove(v1)


# find the force number
finish_flag = True  # if there is only one choice or for each row or column or subbox there is only one possible number
while(finish_flag):
    finish_flag = False
    for k, v in possible_dict.items():
        if len(v) == 1:  # find the definately digit.
            finish_flag = True
            print('☝', k, v)
            # a, b = k  # unpack the location
            # subbox_index = subbox_location_index[k]  # get the sub index
            for i in v:
                value = i  # get the number in set
            update_possible_dict(k, value)

    updatedict = dict()  # date need to be update
    for i in range(9):  # check the row、column and subbox
        row_list = list()
        c_row = Counter()

        column_list = list()
        c_column = Counter()

        subbox_list = list()
        c_subbox = Counter()
        # check the possible number row by row except the given number
        for row_location in row_index_location[i]:
            print(row_location)
            row_list += list(possible_dict[row_location])
        # print('@',row_list)
        c_row = Counter(row_list)
        print(c_row)
        for k1, v1 in c_row.items():
            if v1 == 1:
                print('🍐', k1)
                for row_location in row_index_location[i]:
                    if k1 in possible_dict[row_location]:
                        print('⌛', row_location)  # find the only one in row
                        updatedict[row_location] = k1

        # check the possible number column by row except the given number
        for column_location in column_index_location[i]:
            print(column_location)
            column_list += list(possible_dict[column_location])
        # print('@',row_list)
        c_column = Counter(column_list)
        print(c_column)
        for k2, v2 in c_column.items():
            if v2 == 1:
                print('🍏', k2)
                for column_location in column_index_location[i]:
                    if k2 in possible_dict[column_location]:
                        # find the only one in column
                        print('⌛', column_location)
                        updatedict[column_location] = k2

        # check the possible number column by row except the given number
        for subbox_location in subbox_index_location[i]:
            print(subbox_location)
            subbox_list += list(possible_dict[subbox_location])
        # print('@',row_list)
        c_subbox = Counter(subbox_list)
        print(c_column)
        for k3, v3 in c_subbox.items():
            if v3 == 1:
                print('🍓', k3)
                for subbox_location in subbox_index_location[i]:
                    if k3 in possible_dict[subbox_location]:
                        # find the only one in subbox
                        print('⌛', subbox_location)
                        updatedict[subbox_location] = k3

    print(updatedict)  # TODO: DELETE THE FINAL ONE
    # update the possible_dict
    if updatedict:
        finish_flag = True
    for k1, v1 in updatedict.items():  # update the possible_dict first
        # for k2,v2 in possible_dict.items():
        update_possible_dict(k1, v1)

print(possible_dict)
print(test_matrix_row)
possible_dict
test_matrix_row
sudoku_dict


# generate the marked suduku_dict
def generate_marked_sudoku_dict(sudoku_dict):
    marked_sudoku_dict = deepcopy(sudoku_dict)  # copy the forceed sukuku_dict
    for k, v in possible_dict.items():  # (8, 8) {1, 3, 4, 6}
        print(k, v)
        for cornor_number in v:  # {1, 3, 4, 6}
            marked_sudoku_dict[k][cornor_number] = False  # show in the corner
    return marked_sudoku_dict


generate_marked_sudoku_dict(sudoku_dict)


#%%
# fix read the file without any space
import os
print(os.getcwd())
os.chdir('C:\Study\VScode\Assignment\Assignment2')
print(os.getcwd())


class Sudoku(object):  # Sudoku class
    def __init__(self, *args):
        self.filename = args   # filename
        self.sudoku_list = []  # to store the filestream
        print(args)

        with open(*args, encoding='utf-8') as original_grid:  # open the file
            for digit in original_grid:
                self.sudoku_list.append(
                    ' '.join(digit.strip()).split())  # separate by split
            print(self.sudoku_list)

        L = []  # store the number
        for digit_string in self.sudoku_list:
            for i in digit_string:
                try:
                    L.append(int(i))  # problem if i is letter
                except:
                    raise SudokuError('Incorrect input')
        print(L)


a = Sudoku('sudoku_4.txt')


#%%
# find the preemptive set
from collections import defaultdict
from copy import deepcopy
from collections import Counter

#TODO:sudoku4   pass the test
worked_possible_dict={(0, 0): {2, 4, 6, 7, 8},
 (0, 4): {2, 4, 6, 7},
 (0, 5): {2, 4, 6, 7},
 (0, 6): {1, 6},
 (0, 7): {8, 1, 2},
 (0, 8): {1, 2, 6},
 (1, 0): {2, 4, 5, 6},
 (1, 1): {2, 4, 5, 6},
 (1, 2): set(),
 (1, 4): {2, 3, 4, 6},
 (1, 5): set(),
 (1, 6): {3, 5, 6},
 (1, 8): {2, 6},
 (2, 0): {2, 5, 6, 7, 8},
 (2, 1): {2, 5, 6, 7, 8},
 (2, 2): {8, 2, 5},
 (2, 3): {2, 3, 6},
 (2, 5): {2, 3, 6, 7},
 (2, 7): {8, 2, 3, 5},
 (3, 1): {2, 5, 6, 8, 9},
 (3, 2): {8, 2, 5},
 (3, 4): {2, 5, 6, 7, 8},
 (3, 5): {2, 5, 6, 7},
 (3, 6): {5, 7},
 (3, 7): {9, 2, 5},
 (4, 0): {2, 3, 4, 5, 6, 8, 9},
 (4, 1): {2, 4, 5, 6, 8, 9},
 (4, 2): {2, 3, 4, 5, 8},
 (4, 3): {1, 2, 3, 6, 9},
 (4, 4): {2, 3, 5, 6, 7, 8},
 (4, 5): {2, 3, 5, 6, 7},
 (4, 6): {1, 4, 5, 7},
 (4, 7): {1, 2, 4, 5, 9},
 (4, 8): {1, 2, 9, 7},
 (5, 0): {2, 3, 4, 5, 9},
 (5, 1): {9, 2, 4, 5},
 (5, 3): {1, 2, 3, 9},
 (5, 4): {2, 3, 5},
 (5, 5): {2, 3, 5},
 (5, 8): {1, 2, 9},
 (6, 0): {9, 3, 4, 5},
 (6, 1): {9, 4, 5},
 (6, 4): {3, 4, 5},
 (6, 7): {1, 3, 4, 9},
 (6, 8): {1, 9},
 (7, 0): {2, 3, 4, 7, 8},
 (7, 2): {8, 2, 3, 4},
 (7, 3): {2, 3, 6},
 (7, 5): {2, 3, 4, 6},
 (7, 6): {3, 4, 6, 7},
 (7, 7): {3, 4},
 (8, 0): {2, 3, 4, 5, 7, 9},
 (8, 1): {2, 4, 5, 7, 9},
 (8, 2): {2, 3, 4, 5},
 (8, 3): {2, 3, 6},
 (8, 4): {2, 3, 4, 5, 6},
 (8, 6): {3, 4, 6, 7},
 (8, 7): {9, 3, 4}}
row_index_location={0: [(0, 0), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)], 1: [(1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 8)], 2: [(2, 0), (2, 1), (2, 2), (2, 3), (2, 5), (2, 7)], 3: [(3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7)], 4: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)], 5: [(5, 0), (5, 1), (5, 3), (5, 4), (5, 5), (5, 8)], 6: [(6, 0), (6, 1), (6, 4), (6, 7), (6, 8)], 7: [(7, 0), (7, 2), (7, 3), (7, 5), (7, 6), (7, 7)], 8: [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 6), (8, 7)]}
column_index_location={0: [(0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)], 4: [(0, 4), (1, 4), (3, 4), (4, 4), (5, 4), (6, 4), (8, 4)], 5: [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (7, 5)], 6: [(0, 6), (1, 6), (3, 6), (4, 6), (7, 6), (8, 6)], 7: [(0, 7), (2, 7), (3, 7), (4, 7), (6, 7), (7, 7), (8, 7)], 8: [(0, 8), (1, 8), (4, 8), (5, 8), (6, 8)], 1: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (8, 1)], 2: [(1, 2), (2, 2), (3, 2), (4, 2), (7, 2), (8, 2)], 3: [(2, 3), (4, 3), (5, 3), (7, 3), (8, 3)]}
subbox_index_location={0: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)], 1: [(0, 4), (0, 5), (1, 4), (1, 5), (2, 3), (2, 5)], 2: [(0, 6), (0, 7), (0, 8), (1, 6), (1, 8), (2, 7)], 3: [(3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1)], 4: [(3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)], 5: [(3, 6), (3, 7), (4, 6), (4, 7), (4, 8), (5, 8)], 6: [(6, 0), (6, 1), (7, 0), (7, 2), (8, 0), (8, 1), (8, 2)], 7: [(6, 4), (7, 3), (7, 5), (8, 3), (8, 4)], 8: [(6, 7), (6, 8), (7, 6), (7, 7), (8, 6), (8, 7)]}
worked_sudoku_dict={(0, 0): {1: None, 2: False, 3: None, 4: False, 5: None, 6: False, 7: False, 8: False, 9: None, 10: None}, (0, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 3}, (0, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (0, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (0, 4): {1: None, 2: False, 3: None, 4: False, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (0, 5): {1: None, 2: False, 3: None, 4: False, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (0, 6): {1: False, 2: None, 3: None, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (0, 7): {1: False, 2: False, 3: None, 4: None, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (0, 8): {1: False, 2: False, 3: None, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (1, 0): {1: None, 2: False, 3: None, 4: False, 5: False, 6: False, 7: None, 8: None, 9: None, 10: None}, (1, 1): {1: None, 2: False, 3: None, 4: False, 5: False, 6: False, 7: None, 8: None, 9: None, 10: None}, (1, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (1, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (1, 4): {1: None, 2: False, 3: False, 4: False, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (1, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (1, 6): {1: None, 2: None, 3: False, 4: None, 5: False, 6: False, 7: None, 8: None, 9: None, 10: None}, (1, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (1, 8): {1: None, 2: False, 3: None, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (2, 0): {1: None, 2: False, 3: None, 4: None, 5: False, 6: False, 7: False, 8: False, 9: None, 10: None}, (2, 1): {1: None, 2: False, 3: None, 4: None, 5: False, 6: False, 7: False, 8: False, 9: None, 10: None}, (2, 2): {1: None, 2: False, 3: None, 4: None, 5: False, 6: None, 7: None, 8: False, 9: None, 10: None}, (2, 3): {1: None, 2: False, 3: False, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (2, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (2, 5): {1: None, 2: False, 3: False, 4: None, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (2, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (2, 7): {1: None, 2: False, 3: False, 4: None, 5: False, 6: None, 7: None, 8: False, 9: None, 10: None}, (2, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 4}, (3, 0): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (3, 1): {1: None, 2: False, 3: None, 4: None, 5: False, 6: False, 7: None, 8: False, 9: False, 10: None}, (3, 2): {1: None, 2: False, 3: None, 4: None, 5: False, 6: None, 7: None, 8: False, 9: None, 10: None}, (3, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 4}, (3, 4): {1: None, 2: False, 3: None, 4: None, 5: False, 6: False, 7: False, 8: False, 9: None, 10: None}, (3, 5): {1: None, 2: False, 3: None, 4: None, 5: False, 6: False, 7: False, 8: None, 9: None, 10: None}, (3, 6): {1: None, 2: None, 3: None, 4: None, 5: False, 6: None, 7: False, 8: None, 9: None, 10: None}, (3, 7): {1: None, 2: False, 3: None, 4: None, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (3, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 3}, (4, 0): {1: None, 2: False, 3: False, 4: False, 5: False, 6: False, 7: None, 8: False, 9: False, 10: None}, (4, 1): {1: None, 2: False, 3: None, 4: False, 5: False, 6: False, 7: None, 8: False, 9: False, 10: None}, (4, 2): {1: None, 2: False, 3: False, 4: False, 5: False, 6: None, 7: None, 8: False, 9: None, 10: None}, (4, 3): {1: False, 2: False, 3: False, 4: None, 5: None, 6: False, 7: None, 8: None, 9: False, 10: None}, (4, 4): {1: None, 2: False, 3: False, 4: None, 5: False, 6: False, 7: False, 8: False, 9: None, 10: None}, (4, 5): {1: None, 2: False, 3: False, 4: None, 5: False, 6: False, 7: False, 8: None, 9: None, 10: None}, (4, 6): {1: False, 2: None, 3: None, 4: False, 5: False, 6: None, 7: False, 8: None, 9: None, 10: None}, (4, 7): {1: False, 2: False, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (4, 8): {1: False, 2: False, 3: None, 4: None, 5: None, 6: None, 7: False, 8: None, 9: False, 10: None}, (5, 0): {1: None, 2: False, 3: False, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (5, 1): {1: None, 2: False, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (5, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (5, 3): {1: False, 2: False, 3: False, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (5, 4): {1: None, 2: False, 3: False, 4: None, 5: False, 6: None, 7: None, 8: None, 9: None, 10: None}, (5, 5): {1: None, 2: False, 3: False, 4: None, 5: False, 6: None, 7: None, 8: None, 9: None, 10: None}, (5, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (5, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (5, 8): {1: False, 2: False, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (6, 0): {1: None, 2: None, 3: False, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (6, 1): {1: None, 2: None, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (6, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (6, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (6, 4): {1: None, 2: None, 3: False, 4: False, 5: False, 6: None, 7: None, 8: None, 9: None, 10: None}, (6, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (6, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 2}, (6, 7): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (6, 8): {1: False, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (7, 0): {1: None, 2: False, 3: False, 4: False, 5: None, 6: None, 7: False, 8: False, 9: None, 10: None}, (7, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (7, 2): {1: None, 2: False, 3: False, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (7, 3): {1: None, 2: False, 3: False, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (7, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (7, 5): {1: None, 2: False, 3: False, 4: False, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (7, 6): {1: None, 2: None, 3: False, 4: False, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (7, 7): {1: None, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}, (7, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (8, 0): {1: None, 2: False, 3: False, 4: False, 5: False, 6: None, 7: False, 8: None, 9: False, 10: None}, (8, 1): {1: None, 2: False, 3: None, 4: False, 5: False, 6: None, 7: False, 8: None, 9: False, 10: None}, (8, 2): {1: None, 2: False, 3: False, 4: False, 5: False, 6: None, 7: None, 8: None, 9: None, 10: None}, (8, 3): {1: None, 2: False, 3: False, 4: None, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (8, 4): {1: None, 2: False, 3: False, 4: False, 5: False, 6: False, 7: None, 8: None, 9: None, 10: None}, (8, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (8, 6): {1: None, 2: None, 3: False, 4: False, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (8, 7): {1: None, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (8, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}}


# #TODO: sudoku 5  pass the test !!!!!!!Finish!!!!!!  Crazy!!!!!!!!!
# worked_possible_dict={(0, 0): set(), (0, 2): set(), (0, 4): {3, 4}, (0, 5): {1, 3, 4}, (0, 8): {1, 3, 4}, (1, 0): {4, 7}, (1, 3): set(), (1, 4): set(), (1, 6): {9, 4}, (1, 8): {4, 7}, (2, 1): {4, 7}, (2, 3): {1, 2, 4, 9}, (2, 4): {9, 2, 3, 4}, (2, 5): {1, 2, 3, 4, 9}, (2, 6): {9, 4, 5}, (2, 7): {1, 3, 4, 9}, (2, 8): {1, 3, 4, 5, 7}, (3, 0): {1, 3, 4, 9}, (3, 1): {8, 1, 4}, (3, 3): {9, 2, 4}, (3, 5): {9, 2, 4}, (3, 6): {9, 2, 4}, (3, 7): {1, 3, 4, 8, 9}, (4, 0): {1, 4, 6, 9}, (4, 1): {1, 4, 6}, (4, 2): {9, 2}, (4, 4): set(), (4, 6): {9, 2, 4, 5}, (4, 7): {1, 4, 9}, (4, 8): {1, 4, 5}, (5, 1): {8, 4}, (5, 2): {8, 9, 2, 3}, (5, 3): {9, 2, 4}, (5, 5): set(), (5, 7): {8, 9, 3, 4}, (5, 8): {8, 3, 4}, (6, 0): {3, 6, 7}, (6, 1): {8, 6, 7}, (6, 2): {8, 3}, (6, 3): set(), (6, 4): {2, 3, 4, 7}, (6, 5): {2, 3, 4}, (6, 7): {8, 4}, (7, 0): {1, 9, 7}, (7, 2): {8, 9}, (7, 4): {9, 4, 7}, (7, 5): {1, 4, 9}, (7, 8): {8, 4}, (8, 0): {1, 3, 9}, (8, 3): {1, 9}, (8, 4): {9, 3}, (8, 6): set(), (8, 8): set()}
# row_index_location={0: [(0, 0), (0, 2), (0, 4), (0, 5), (0, 8)], 1: [(1, 0), (1, 3), (1, 4), (1, 6), (1, 8)], 2: [(2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], 3: [(3, 0), (3, 1), (3, 3), (3, 5), (3, 6), (3, 7)], 4: [(4, 0), (4, 1), (4, 2), (4, 4), (4, 6), (4, 7), (4, 8)], 5: [(5, 1), (5, 2), (5, 3), (5, 5), (5, 7), (5, 8)], 6: [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7)], 7: [(7, 0), (7, 2), (7, 4), (7, 5), (7, 8)], 8: [(8, 0), (8, 3), (8, 4), (8, 6), (8, 8)]}
# column_index_location={0: [(0, 0), (1, 0), (3, 0), (4, 0), (6, 0), (7, 0), (8, 0)], 2: [(0, 2), (4, 2), (5, 2), (6, 2), (7, 2)], 4: [(0, 4), (1, 4), (2, 4), (4, 4), (6, 4), (7, 4), (8, 4)], 5: [(0, 5), (2, 5), (3, 5), (5, 5), (6, 5), (7, 5)], 8: [(0, 8), (1, 8), (2, 8), (4, 8), (5, 8), (7, 8), (8, 8)], 3: [(1, 3), (2, 3), (3, 3), (5, 3), (6, 3), (8, 3)], 6: [(1, 6), (2, 6), (3, 6), (4, 6), (8, 6)], 1: [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1)], 7: [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7)]}
# subbox_index_location={0: [(0, 0), (0, 2), (1, 0), (2, 1)], 1: [(0, 4), (0, 5), (1, 3), (1, 4), (2, 3), (2, 4), (2, 5)], 2: [(0, 8), (1, 6), (1, 8), (2, 6), (2, 7), (2, 8)], 3: [(3, 0), (3, 1), (4, 0), (4, 1), (4, 2), (5, 1), (5, 2)], 4: [(3, 3), (3, 5), (4, 4), (5, 3), (5, 5)], 5: [(3, 6), (3, 7), (4, 6), (4, 7), (4, 8), (5, 7), (5, 8)], 6: [(6, 0), (6, 1), (6, 2), (7, 0), (7, 2), (8, 0)], 7: [(6, 3), (6, 4), (6, 5), (7, 4), (7, 5), (8, 3), (8, 4)], 8: [(6, 7), (7, 8), (8, 6), (8, 8)]}
# worked_sudoku_dict={(0, 0): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 2}, (0, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (0, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (0, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (0, 4): {1: None, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}, (0, 5): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}, (0, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (0, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (0, 8): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}, (1, 0): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: False, 8: None, 9: None, 10: None}, (1, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 3}, (1, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (1, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (1, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (1, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (1, 6): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (1, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 2}, (1, 8): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: False, 8: None, 9: None, 10: None}, (2, 0): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (2, 1): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: False, 8: None, 9: None, 10: None}, (2, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (2, 3): {1: False, 2: False, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (2, 4): {1: None, 2: False, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (2, 5): {1: False, 2: False, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (2, 6): {1: None, 2: None, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (2, 7): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (2, 8): {1: False, 2: None, 3: False, 4: False, 5: False, 6: None, 7: False, 8: None, 9: None, 10: None}, (3, 0): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (3, 1): {1: False, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (3, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (3, 3): {1: None, 2: False, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (3, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (3, 5): {1: None, 2: False, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (3, 6): {1: None, 2: False, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (3, 7): {1: False, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: False, 9: False, 10: None}, (3, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (4, 0): {1: False, 2: None, 3: None, 4: False, 5: None, 6: False, 7: None, 8: None, 9: False, 10: None}, (4, 1): {1: False, 2: None, 3: None, 4: False, 5: None, 6: False, 7: None, 8: None, 9: None, 10: None}, (4, 2): {1: None, 2: False, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (4, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 3}, (4, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (4, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (4, 6): {1: None, 2: False, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: False, 10: None}, (4, 7): {1: False, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (4, 8): {1: False, 2: None, 3: None, 4: False, 5: False, 6: None, 7: None, 8: None, 9: None, 10: None}, (5, 0): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (5, 1): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (5, 2): {1: None, 2: False, 3: False, 4: None, 5: None, 6: None, 7: None, 8: False, 9: False, 10: None}, (5, 3): {1: None, 2: False, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (5, 4): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (5, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (5, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (5, 7): {1: None, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: False, 9: False, 10: None}, (5, 8): {1: None, 2: None, 3: False, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (6, 0): {1: None, 2: None, 3: False, 4: None, 5: None, 6: False, 7: False, 8: None, 9: None, 10: None}, (6, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: False, 7: False, 8: False, 9: None, 10: None}, (6, 2): {1: None, 2: None, 3: False, 4: None, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (6, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (6, 4): {1: None, 2: False, 3: False, 4: False, 5: None, 6: None, 7: False, 8: None, 9: None, 10: None}, (6, 5): {1: None, 2: False, 3: False, 4: False, 5: None, 6: None, 7: None, 8: None, 9: None, 10: None}, (6, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 1}, (6, 7): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (6, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 9}, (7, 0): {1: False, 2: None, 3: None, 4: None, 5: None, 6: None, 7: False, 8: None, 9: False, 10: None}, (7, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 2}, (7, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: False, 9: False, 10: None}, (7, 3): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (7, 4): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: False, 8: None, 9: False, 10: None}, (7, 5): {1: False, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (7, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 3}, (7, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (7, 8): {1: None, 2: None, 3: None, 4: False, 5: None, 6: None, 7: None, 8: False, 9: None, 10: None}, (8, 0): {1: False, 2: None, 3: False, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (8, 1): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 5}, (8, 2): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 4}, (8, 3): {1: False, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (8, 4): {1: None, 2: None, 3: False, 4: None, 5: None, 6: None, 7: None, 8: None, 9: False, 10: None}, (8, 5): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 8}, (8, 6): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 6}, (8, 7): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 7}, (8, 8): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: 2}}






subbox_location_index = dict()
def generate_subbox_location_index():
    for y in range(9):
        for x in range(9):
            subbox_location_index[(y, x)] = y // 3 * 3 + \
                x // 3  # add subindex to location
generate_subbox_location_index()

#preemative number
def delete_row_dict(preemative_dict, possible_dict):# update the dict by the rule of preemptive  
    for k,v in preemative_dict.items():
        print(k,v)
        for preemative_location in v:
            y,x=preemative_location            
        row_check=set(row_index_location[y])-set(v)        
        print(set(row_index_location[y]))
        print(row_check)
        for i in row_check:  #TODO:SELF
            for v1 in k:
                if v1 in possible_dict[i]:  # update the row
                    print('🍣', i,v1)
                    possible_dict[i].remove(v1)
                    worked_sudoku_dict[i][v1]=True # mark cancel

def delete_column_dict(preemative_dict, possible_dict): # update the dict by the rule of preemptive 
    for k,v in preemative_dict.items():
        print(k,v)        
        for preemative_location in v:
            y,x=preemative_location
        column_check=set(column_index_location[x])-set(v)
        print('#',column_check)
        #print(k)
        #print(i)
        for i in column_check: #TODO:SELF
            print('⌚',i)
            print(possible_dict[i])
            for v1 in k:
                print('⏩',v1)
                if v1 in possible_dict[i]:  # update the column
                    print('🍚', i,v1)
                    possible_dict[i].remove(v1)
                    worked_sudoku_dict[i][v1]=True # mark cancel

def delete_subbox_dict(preemative_dict, possible_dict): # update the dict by the rule of preemptive 
    for k,v in preemative_dict.items():
        print('Ⓜ',k,v)
        for preemative_location in v:
            y,x=preemative_location
        subbox_index = subbox_location_index[preemative_location]  # get the sub index TODO:SELF
        subbox_check=set(subbox_index_location[subbox_index])-set(v)
        print('@',subbox_check)
        for i in subbox_check: #TODO:SELF
            for v1 in k:
                if v1 in possible_dict[i]:  # update the subbox
                    print('🍕', i,v1)
                    possible_dict[i].remove(v1) # delete the preemptive rule number
                    worked_sudoku_dict[i][v1]=True # mark cancel



# find all the preemative number 
# check the preemative by row
def preemative_pair():
    preemative_dict=dict()
    for i in range(9): # search all the subbox
        for select_location in row_index_location[i]:
            preemative_sum=0 #number of subset 
            a=[] #subset
            a.append(worked_possible_dict[select_location]) 
            b=[] #location of subset
            b.append(select_location)
            for compare_location in row_index_location[i]:
                if worked_possible_dict[compare_location]: #empty set is also the subset of any set,get rid of it
                    if worked_possible_dict[select_location]>=worked_possible_dict[compare_location]:# find a set has subset
                        preemative_sum+=1 #number of subset +1
                        a.append(worked_possible_dict[compare_location]) # add this set
                        b.append(compare_location) # add the location of this set
                        if preemative_sum == len(worked_possible_dict[select_location]):# when counter exclude itself  the defination of preemative set
                            if set(row_index_location[i])-set(b): # ensure it is not all of the empty set
                                flag=0 # count the found number in difference
                                for difference in set(row_index_location[i])-set(b):
                                    if not worked_possible_dict[difference]: #(1, 2): set()  
                                        flag+=1
                                if flag!=len(set(row_index_location[i])-set(b)): # not all the preemative is founed location           
                                    print('☔',worked_possible_dict[select_location]) # preemative set
                                    print(set(row_index_location[i])-set(b)) # may need to cancel some number
                                    print(a) # all the subset
                                    print(b) #all the location
                                    preemative_dict[tuple(worked_possible_dict[select_location])]=list(b)
    delete_row_dict(preemative_dict, worked_possible_dict) # delete the preemative set in the same row
    
    # check the preemative by column
    preemative_dict=dict()
    for i in range(9): # search all the subbox
        for select_location in column_index_location[i]:
            preemative_sum=0 #number of subset 
            a=[] #subset
            a.append(worked_possible_dict[select_location]) 
            b=[] #location of subset
            b.append(select_location)
            for compare_location in column_index_location[i]:
                if worked_possible_dict[compare_location]: #empty set is also the subset of any set,get rid of it
                    if worked_possible_dict[select_location]>=worked_possible_dict[compare_location]:# find a set has subset #TODO:it's possible equal
                        preemative_sum+=1 #number of subset +1
                        a.append(worked_possible_dict[compare_location]) # add this set
                        b.append(compare_location) # add the location of this set
                        if preemative_sum == len(worked_possible_dict[select_location]):# when counter exclude itself  the defination of preemative set
                            if set(column_index_location[i])-set(b): # ensure it is not all of the empty set
                                flag=0
                                for difference in set(column_index_location[i])-set(b):
                                    if not worked_possible_dict[difference]:
                                        flag+=1

                                #print('@',len(set(column_index_location[i])-set(b)))
                                if flag!=len(set(column_index_location[i])-set(b)):            
                                    print('☕',worked_possible_dict[select_location]) # preemative set
                                    print(set(column_index_location[i])-set(b)) # may need to cancel some number
                                    print(a) # all the subset
                                    print(b) #all the location
                                    preemative_dict[tuple(worked_possible_dict[select_location])]=b
    delete_column_dict(preemative_dict, worked_possible_dict) # delete the preemative set in the same column
    # search the preemative set by subbox
    preemative_dict=dict()
    for i in range(9): # search all the subbox
    
        for select_location in subbox_index_location[i]:
            preemative_sum=0 #number of subset 
            a=[] #subset
            a.append(worked_possible_dict[select_location]) 
            b=[] #location of subset
            b.append(select_location)
            for compare_location in subbox_index_location[i]:
                if worked_possible_dict[compare_location]: #empty set is also the subset of any set,get rid of it
                    if worked_possible_dict[select_location]>=worked_possible_dict[compare_location]:# find a set has subset
                        preemative_sum+=1 #number of subset +1
                        a.append(worked_possible_dict[compare_location]) # add this set
                        b.append(compare_location) # add the location of this set
                        if preemative_sum == len(worked_possible_dict[select_location]):# when counter exclude itself  the defination of preemative set
                            if set(subbox_index_location[i])-set(b): # ensure it is not all of the empty set
                                flag=0
                                for difference in set(subbox_index_location[i])-set(b):
                                    if not worked_possible_dict[difference]:
                                        flag+=1
                                if flag!=len(set(subbox_index_location[i])-set(b)):
                                    print('☁',worked_possible_dict[select_location]) # preemative set
                                    print(set(subbox_index_location[i])-set(b)) # may need to cancel some number
                                    print(a) # all the subset
                                    print(b) #all the location
                                    preemative_dict[tuple(worked_possible_dict[select_location])]=b
    delete_subbox_dict(preemative_dict, worked_possible_dict) # delete the preemative set in the same subbox
    #print('#',preemative_dict)
    #return preemative_dict                   


# find the forced number
def find_forced_number(possible_dict,forced_sudoku_dict):
    # find the force number
    finish_flag = True  # if there is only one choice or for each row or column or subbox there is only one possible number
    while(finish_flag):
        finish_flag = False
        for k, v in possible_dict.items():
            if len(v) == 1:  # find the definately digit.
                finish_flag = True
                print('☝', k, v)
                # a, b = k  # unpack the location
                # subbox_index = subbox_location_index[k]  # get the sub index
                for i in v:
                    value = i  # get the number in set
                update_possible_dict(
                    possible_dict,forced_sudoku_dict, k, value)

        # date need to be update TODO:change to defaultdict(list) for counting
        temp_updatedict = defaultdict(list)
        updatedict = dict()
        for i in range(9):  # check the row、column and subbox
            # #TODO: It's not necessary to check the c_row and column here when finding the force number
            row_list = list()
            c_row = Counter()

            column_list = list()
            c_column = Counter()

            subbox_list = list()
            c_subbox = Counter()
            # check the possible number row by row except the given number
            #TODO: It's not necessary to check the c_row and column here when finding the force number
            for row_location in row_index_location[i]:
                print(row_location)
                row_list += list(possible_dict[row_location])
            # print('@',row_list)
            c_row = Counter(row_list)
            print(c_row)
            for k1, v1 in c_row.items(): 
                if v1 == 1:
                    print('🍐', k1)
                    for row_location in row_index_location[i]:
                        if k1 in possible_dict[row_location]:
                            # find the only one in row
                            print('⌛', row_location)
                            temp_updatedict[row_location].append(
                                k1)  # append for counting

            # check the possible number column by row except the given number
            for column_location in column_index_location[i]:
                print(column_location)
                column_list += list(
                    possible_dict[column_location])
            # print('@',row_list)
            c_column = Counter(column_list)
            print(c_column)
            for k2, v2 in c_column.items():
                if v2 == 1:
                    print('🍏', k2)
                    for column_location in column_index_location[i]:
                        if k2 in possible_dict[column_location]:
                            # find the only one in column
                            print('⌛', column_location)
                            temp_updatedict[column_location].append(  
                                k2)  # append for counting

            # check the possible number column by row except the given number
            for subbox_location in subbox_index_location[i]:
                print(subbox_location)
                subbox_list += list(
                    possible_dict[subbox_location])
            # print('@',row_list)
            c_subbox = Counter(subbox_list)
            #print(c_column)
            for k3, v3 in c_subbox.items():
                if v3 == 1:
                    print('🍓', k3)
                    for subbox_location in subbox_index_location[i]:
                        if k3 in possible_dict[subbox_location]:
                            # find the only one in subbox
                            print('⌛', subbox_location)
                            # append for counting
                            updatedict[subbox_location] = k3

        #TODO: It's not necessary to check the c_row and column here when finding the force number                    
        for k, v in temp_updatedict.items(): #could use for worked tex
            #if len(v) == 2:  # exactly the forced one
                updatedict[k] = v[0]

        print(updatedict)  # TODO: DELETE THE FINAL ONE
        # update the possible_dict
        if updatedict:
            finish_flag = True
        for k1, v1 in updatedict.items():  # update the possible_dict first
            # for k2,v2 in possible_dict.items():
            update_possible_dict(
                possible_dict, forced_sudoku_dict, k1, v1)

def update_possible_dict(possible_dict, sudoku_dict, k1, v1):
        y, x = k1
        #test_matrix_row[y][x] = v1
        sudoku_dict[k1][10] = v1  # update the out_put latex dict
        #TODO: make other cancel
        for i in range(1,10):
            if worked_sudoku_dict[k1][i]==False: # cancel the rest
                worked_sudoku_dict[k1][i]=True
        possible_dict[k1] = set()  # delete the found number
        # update the line row and subbox
        subbox_index = subbox_location_index[k1]  # get the sub index
        for i in row_index_location[y]:
            if v1 in possible_dict[i]:  # update the row
                print('🍣', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)
                worked_sudoku_dict[i][v1]=True # mark cancel
        for i in column_index_location[x]:
            if v1 in possible_dict[i]:  # update the column
                print('🍚', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)
                worked_sudoku_dict[i][v1]=True # mark cancel
        for i in subbox_index_location[subbox_index]:
            if v1 in possible_dict[i]:  # update the subbox
                print('🍕', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)
                worked_sudoku_dict[i][v1]=True # mark cancel

#preemative_pair() # first preemptive
#print(worked_possible_dict) # dict after update by preemative rule
#find_forced_number(worked_possible_dict,worked_sudoku_dict) #
#preemative_pair() #check second time
#find_forced_number(worked_possible_dict,worked_sudoku_dict) # Done
#preemative_pair()
#find_forced_number(worked_possible_dict,worked_sudoku_dict)

Temp_worked_sudoku_dict=defaultdict()
while(Temp_worked_sudoku_dict!=worked_sudoku_dict):
    preemative_pair()
    Temp_worked_sudoku_dict=deepcopy(worked_sudoku_dict)
    find_forced_number(worked_possible_dict,worked_sudoku_dict)
    































# generate the tex for checking
import os
print(os.getcwd())
os.chdir('C:\Study\VScode\Assignment\Assignment2')
# initial comment in tex
initial_comment = r"""\documentclass[10pt]{article}
\usepackage[left=0pt,right=0pt]{geometry}
\usepackage{tikz}
\usetikzlibrary{positioning}
\usepackage{cancel}
\pagestyle{empty}

\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},
                               label=above right:{\tiny #2},
                               label=below left:{\tiny #3},
                               label=below right:{\tiny #4}]{#5};}}

\begin{document}

\tikzset{every node/.style={minimum size=.5cm}}

\begin{center}
\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline"""

# finalize comment in tex
finalize_comment = r"""
\end{tabular}
\end{center}

\end{document}
"""

def tex_output(sudoku_dict, specific_name):
    initial = []  # string list to store the output comment
    sudoku_dict = sudoku_dict
    # generate the  tex from a dictionary

    def generate_tex():
        sudoku_string = []
        for line in range(0, 9):  # row
            sudoku_string.append('\n')
            sudoku_string.append('% Line ' + f'{line+1}' + '\n')
            for col in range(0, 9):
                middle_digit = None
                upper_left_corner = []
                temp_dict = dict()
                upper_left_corner = ''
                upper_right_corner = ''
                lower_left_corner = ''
                lower_right_corner = ''
                if sudoku_dict[line, col][10]:  # if the middle number has been decided
                    middle_digit = sudoku_dict[line, col][10]

                # if the middle number has been decided
                for k, v in sorted(sudoku_dict[line, col].items()):
                    if v == True and k <= 9:  # cancel one
                        temp_dict[k] = '\\cancel' + '{' + str(k) + '}'
                    if v == False and k <= 9:  # kept one
                        temp_dict[k] = str(k)

                for k, v in sorted(temp_dict.items()):
                    if k in range(1, 3):
                        upper_left_corner += ' ' + temp_dict[k]
                    if k in range(3, 5):
                        upper_right_corner += ' ' + temp_dict[k]
                    if k in range(5, 7):
                        lower_left_corner += ' ' + temp_dict[k]
                    if k in range(7, 10):
                        lower_right_corner += ' ' + temp_dict[k]

                sudoku_string.append('\\N')
                if upper_left_corner:
                    sudoku_string.append(
                        '{'f'{upper_left_corner.strip()}''}')
                else:
                    sudoku_string.append('{}')  # upper left corner
                if upper_right_corner:
                    sudoku_string.append(
                        '{'f'{upper_right_corner.strip()}''}')
                else:
                    sudoku_string.append('{}')  # upper right corner
                if lower_left_corner:
                    sudoku_string.append(
                        '{'f'{lower_left_corner.strip()}''}')
                else:
                    sudoku_string.append('{}')  # lower left corner
                if lower_right_corner:
                    sudoku_string.append(
                        '{'f'{lower_right_corner.strip()}''}')
                else:
                    sudoku_string.append('{}')  # lower right corner
                if middle_digit:  # out put the middle number
                    sudoku_string.append('{'f'{middle_digit}''}')
                else:
                    sudoku_string.append('{}')
                if col in (0, 1, 3, 4, 6, 7):
                    sudoku_string.append(' & ')
                if col in (2, 5):
                    # at the end don't need the space
                    sudoku_string.append(' &')
                    sudoku_string.append('\n')
            if line in (2, 5):  # print(double line)
                sudoku_string.append(" \\\ \hline\hline")
                sudoku_string.append('\n')
            if line == 8:  # print(double line)
                sudoku_string.append(" \\\ \hline\hline")
            if line in (0, 1, 3, 4, 6, 7):
                sudoku_string.append(" \\\ \hline")
                sudoku_string.append('\n')
        return sudoku_string
    # generate the sudoku_list which like['ab','cd','ef']
    sudoku_comment = generate_tex()
    # merge the sudoku_list['abcdef']
    sudoku_comment = ''.join(sudoku_comment)

    def initialize():
        initial.append(initial_comment)

    def add_sudoku(string_list):
        initial.append(string_list)

    def finalize():
        initial.append(finalize_comment)

    initialize()
    add_sudoku(sudoku_comment)
    finalize()
    # merge  initial_comment+sudoku_comment+finalize_comment
    initial = "".join(initial)
    # sudoku_3_specific.tex
    file_name = 'lalalala' + specific_name + '.tex'
    with open(file_name, 'w') as f:
        f.write(initial)

tex_output(worked_sudoku_dict,'_worked4_test') # test work_test










#%%
def delete_possible_dict(preemative_dict, possible_dict):#, sudoku_dict): 
    delete_list=defaultdict(set)   
    for k,v in preemative_dict.items():
        print(k,v)
        
        for preemative_location in v:
            y,x=preemative_location
            
            row_check=set(row_index_location[y])-set(v)
            column_check=set(column_index_location[x])-set(v)
            subbox_index = subbox_location_index[preemative_location]  # get the sub index TODO:SELF
            subbox_check=set(subbox_index_location[subbox_index])-set(v)
            # update the line row and subbox
            print(set(row_index_location[y]))
            print(row_check)
            # for i in row_check:  #TODO:SELF
            #     for v1 in possible_dict[preemative_location]:
            #         if v1 in possible_dict[i]:  # update the row
            #             print('🍣', i,v1)
            #             # possible_dict[i]-{int(str(*v))}
            #             delete_list[i].add(v1)
            #             #possible_dict[i].remove(v1)
            
            # print('#',column_check)
            # print(k)
            # print(i)
            # for i in column_check: #TODO:SELF
            #     print('⌚',i)
            #     print(possible_dict[i])
            #     for v1 in possible_dict[i]:
            #         print('⏩',v1)
            #         if v1 in possible_dict[preemative_location]:  # update the column
            #             print('🍚', i,v1)

            #             # possible_dict[i]-{int(str(*v))}
            #             delete_list[i].add(v1)
            #             #possible_dict[i].remove(v1)
            
            print('@',subbox_check)
            for i in subbox_check: #TODO:SELF
                for v1 in possible_dict[preemative_location]:
                    if v1 in possible_dict[i]:  # update the subbox
                        print('🍕', i,v1)
                        # possible_dict[i]-{int(str(*v))}
                        delete_list[i].add(v1)
                        #possible_dict[i].remove(v1)
    print(delete_list) 
    for k,v in delete_list.items(): #delete from the possible_dict
        possible_dict[k]-=v
    print(possible_dict)
#delete_possible_dict(preemative_dict, worked_possible_dict)
#print(possible_dict)


#%%
# delete the row、column、subbox
#separate to three
def delete_row_dict(preemative_dict, possible_dict):#, sudoku_dict):    
    for k,v in preemative_dict.items():
        print(k,v)
        for preemative_location in v:
            y,x=preemative_location            
            row_check=set(row_index_location[y])-set(v)        
            print(set(row_index_location[y]))
            print(row_check)
            for i in row_check:  #TODO:SELF
                for v1 in k:
                    if v1 in possible_dict[i]:  # update the row
                        print('🍣', i,v1)

def delete_column_dict(preemative_dict, possible_dict):
    for k,v in preemative_dict.items():
        print(k,v)        
        for preemative_location in v:
            y,x=preemative_location
            column_check=set(column_index_location[x])-set(v)
            print('#',column_check)
            print(k)
            print(i)
            for i in column_check: #TODO:SELF
                print('⌚',i)
                print(possible_dict[i])
                for v1 in k:
                    print('⏩',v1)
                    if v1 in possible_dict[i]:  # update the column
                        print('🍚', i,v1)

def delete_subbox_dict(preemative_dict, possible_dict):
    for k,v in preemative_dict.items():
        print('Ⓜ',k,v)
        for preemative_location in v:
            y,x=preemative_location
            subbox_index = subbox_location_index[preemative_location]  # get the sub index TODO:SELF
            subbox_check=set(subbox_index_location[subbox_index])-set(v)
            print('@',subbox_check)
            for i in subbox_check: #TODO:SELF
                for v1 in k:
                    if v1 in possible_dict[i]:  # update the subbox
                        print('🍕', i,v1)

#%%
a={1,2}
b={2,6}
c={1,2,6}
d={1,2,7}
e=set()
print(a>b)
print(b>a)
print(c>a)
print(c>b)
print(c>d)
print(c>e)
if e:
    print(1)

