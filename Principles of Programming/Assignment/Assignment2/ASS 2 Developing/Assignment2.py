'''
COMP9021 Assignment 2

Sudoku

'''
from collections import defaultdict
from copy import deepcopy
from collections import Counter

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
                self.sudoku_list.append(' '.join(digit.strip()).split())  # separate by split
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
        # change to self in order to use in other function
        self.matrix = tuple(L[i:i + n] for i in range(0, len(L), n))

        print(L)
        print(len(L))  # check the number of the list
        print(self.matrix)

        if(len(L)) != 81:
            raise SudokuError('Incorrect input')

    def preassess(self):  # pretest if the it is a sudoku problem
        print(self.matrix)
        matrix = self.matrix
        self.matrix_row = list(matrix)  # row matrix  used in bare_tex_output
        self.matrix_column = list(map(list, zip(*matrix)))  # column matrix
        merged_matrix = sum(matrix, [])
        tri_matrix = [merged_matrix[i:i + 3]  # separate to 3
                      for i in range(0, len(merged_matrix), 3)]
        self.subbox = [sum(tri_matrix[i:i + 9:3], [])  # subbox matrix
                       for a in (0, 9, 18)for i in range(a, a + 3)]
        print(self.matrix_row)
        print(self.matrix_column)
        print(self.subbox)
        for a in self.matrix_row:  # matrix group by row
            check_list = []
            for i in a:  # each number
                if i == 0:  # do not check zero
                    continue
                else:
                    check_list.append(i)
            print('A', check_list)
            if len(check_list) != len(set(check_list)):  # only once
                print('There is clearly no solution')
                return

        for b in self.matrix_column:  # matrix group by column
            check_list = []
            for i in b:  # each number
                if i == 0:  # do not check zero
                    continue
                else:
                    check_list.append(i)
            print('B', check_list)
            if len(check_list) != len(set(check_list)):  # only once
                print('There is clearly no solution')
                return

        check_list = []
        for c in self.subbox:  # matrix group by subbox
            check_list = []
            for i in c:  # each number
                if i == 0:  # do not check zero
                    continue
                else:
                    check_list.append(i)
            print('C', check_list)
            if len(check_list) != len(set(check_list)):  # only once
                print('There is clearly no solution')
                return
        print('There might be a solution')

    def bare_tex_output(self):  # output the bare_tex
        matrix = self.matrix_row  # get from the def preassess
        print('@@', matrix)

        # generate the original empty data_dict
        #(row_number, column_number): {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 10: middle_number}
        # None : Nothing     False : exist    True :cancel
        self.sudoku_dict = dict()
        box = dict()  # each small box
        for y in range(9):
            for x in range(9):
                for i in range(1, 11):  # 1-9 is the number in the corner,10 is the middle number
                    box[i] = None  # None  True：mark  False：exist
                # deepcopy the  box otherwise if one change all change
                self.sudoku_dict[(y, x)] = deepcopy(box)

        # generate the bare sudo dictionary
        for row_index, row in enumerate(self.matrix_row):
            for column_index, i in enumerate(row):
                # print(row_index,column_index,i)
                if i != 0:
                    self.sudoku_dict[row_index, column_index][10] = i
        print(self.sudoku_dict)
        # TODO: DELETE THE _test
        self.tex_output(self.sudoku_dict, '_bare_test')

    def tex_output(self, sudoku_dict, specific_name):
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
        file_name = list(self.filename)[0][:-4] + specific_name + '.tex'
        with open(file_name, 'w') as f:
            f.write(initial)

    def forced_tex_output(self):  # output the forced_tex
        self.subbox_location_index = dict()  # location to subindex
        matrix_row = self.matrix_row
        matrix_column = self.matrix_column
        subbox = self.subbox
        # TODO: the situation that bare has already been run
        self.forced_sudoku_dict = deepcopy(self.sudoku_dict)
        # generate the subbox_index for check if number in subbox
        # generate a dict that contain the location of each subbox

        def generate_subbox_location_index():
            for y in range(9):
                for x in range(9):
                    self.subbox_location_index[(y, x)] = y // 3 * 3 + \
                        x // 3  # add subindex to location
            # subbox_location_index  # (0, 8): 2

        # generate the dict index of each line and each row in order to force check in the sudoku_dict
        # generate all possible number in each subbox
        self.row_index_location = defaultdict(
            list)  # initial the row_index_location
        self.column_index_location = defaultdict(
            list)  # initial the column_location
        # 0:(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)......
        self.subbox_index_location = defaultdict(list)
        self.possible_dict = dict()

        def all_possile_dict():
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
                    for sb in subbox[self.subbox_location_index[y, x]]:
                        if sb != 0:
                            temp_set.add(sb)
                    print(y, x, temp_set)
                    if flag:  # check if the number has been given
                        continue
                    self.possible_dict[y, x] = set(range(1, 10)) - temp_set
                    # DO NOT CHECK THE GIVEN BOX
                    self.row_index_location[y].append(
                        (y, x))  # add location to row_index
                    self.column_index_location[x].append(
                        (y, x))  # add location to column_index
                    # add location to subindex
                    self.subbox_index_location[y //
                                               3 * 3 + x // 3].append((y, x))

        # use self.possible_dict check the force sudomateix
        self.test_matrix_row = deepcopy(self.matrix_row)

        def find_forced_number():
            # find the force number
            finish_flag = True  # if there is only one choice or for each row or column or subbox there is only one possible number
            while(finish_flag):
                finish_flag = False
                for k, v in self.possible_dict.items():
                    if len(v) == 1:  # find the definately digit.
                        finish_flag = True
                        print('☝', k, v)
                        # a, b = k  # unpack the location
                        # subbox_index = subbox_location_index[k]  # get the sub index
                        for i in v:
                            value = i  # get the number in set
                        self.update_possible_dict(
                            self.possible_dict, self.forced_sudoku_dict, k, value)

                # date need to be update TODO:change to defaultdict(list) for counting
                temp_updatedict = defaultdict(list)
                updatedict = dict()
                for i in range(9):  # check the row、column and subbox
                    # #TODO: It's not necessary to check the c_row and column here when finding the force number
                    # row_list = list()
                    # c_row = Counter()

                    # column_list = list()
                    # c_column = Counter()

                    subbox_list = list()
                    c_subbox = Counter()
                    # check the possible number row by row except the given number
                    #TODO: It's not necessary to check the c_row and column here when finding the force number
                    # for row_location in self.row_index_location[i]:
                    #     print(row_location)
                    #     row_list += list(self.possible_dict[row_location])
                    # # print('@',row_list)
                    # c_row = Counter(row_list)
                    # print(c_row)
                    # for k1, v1 in c_row.items(): 
                    #     if v1 == 1:
                    #         print('🍐', k1)
                    #         for row_location in self.row_index_location[i]:
                    #             if k1 in self.possible_dict[row_location]:
                    #                 # find the only one in row
                    #                 print('⌛', row_location)
                    #                 #temp_updatedict[row_location].append(
                    #                    # k1)  # append for counting

                    # # check the possible number column by row except the given number
                    # for column_location in self.column_index_location[i]:
                    #     print(column_location)
                    #     column_list += list(
                    #         self.possible_dict[column_location])
                    # # print('@',row_list)
                    # c_column = Counter(column_list)
                    # print(c_column)
                    # for k2, v2 in c_column.items():
                    #     if v2 == 1:
                    #         print('🍏', k2)
                    #         for column_location in self.column_index_location[i]:
                    #             if k2 in self.possible_dict[column_location]:
                    #                 # find the only one in column
                    #                 print('⌛', column_location)
                    #                 #temp_updatedict[column_location].append(  
                    #                     #k2)  # append for counting

                    # check the possible number column by row except the given number
                    for subbox_location in self.subbox_index_location[i]:
                        print(subbox_location)
                        subbox_list += list(
                            self.possible_dict[subbox_location])
                    # print('@',row_list)
                    c_subbox = Counter(subbox_list)
                    #print(c_column)
                    for k3, v3 in c_subbox.items():
                        if v3 == 1:
                            print('🍓', k3)
                            for subbox_location in self.subbox_index_location[i]:
                                if k3 in self.possible_dict[subbox_location]:
                                    # find the only one in subbox
                                    print('⌛', subbox_location)
                                    # append for counting
                                    updatedict[subbox_location] = k3

                # TODO: It's not necessary to check the c_row and column here when finding the force number                    
                # for k, v in temp_updatedict.items():
                #     if len(v) == 2:  # exactly the forced one
                #         updatedict[k] = v[0]

                print(updatedict)  # TODO: DELETE THE FINAL ONE
                # update the possible_dict
                if updatedict:
                    finish_flag = True
                for k1, v1 in updatedict.items():  # update the possible_dict first
                    # for k2,v2 in possible_dict.items():
                    self.update_possible_dict(
                        self.possible_dict, self.forced_sudoku_dict, k1, v1)

        generate_subbox_location_index()
        print(self.subbox_location_index)
        all_possile_dict()
        find_forced_number()
        print('⚡', self.forced_sudoku_dict)
        # self.forced_sudoku_dict=deepcopy(self.sudoku_dict)
        # TODO: DELETE THE _test
        self.tex_output(self.forced_sudoku_dict, '_forced_test')

    def marked_tex_output(self):  # output the marked_tex
        self.forced_tex_output()  # TODO: run forced_tex_output to get the forced_sudoku_dict
        self.marked_sudoku_dict = deepcopy(
            self.forced_sudoku_dict)  # copy the forced_sudoku_dict
        # (8, 8) {1, 3, 4, 6}  #TODO: make possible_dict  self
        for k, v in self.possible_dict.items():
            print(k, v)
            for cornor_number in v:  # {1, 3, 4, 6}
                # show in the corner
                self.marked_sudoku_dict[k][cornor_number] = False
        print('⛔', self.marked_sudoku_dict)
        # TODO: DELETE THE _test
        self.tex_output(self.marked_sudoku_dict, '_marked_test')

    def update_possible_dict(self, possible_dict, sudoku_dict, k1, v1):
        y, x = k1
        self.test_matrix_row[y][x] = v1
        sudoku_dict[k1][10] = v1  # update the out_put latex dict
        possible_dict[k1] = set()  # delete the found number
        # update the line row and subbox
        subbox_index = self.subbox_location_index[k1]  # get the sub index
        for i in self.row_index_location[y]:
            if v1 in possible_dict[i]:  # update the row
                print('🍣', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)
        for i in self.column_index_location[x]:
            if v1 in possible_dict[i]:  # update the column
                print('🍚', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)
        for i in self.subbox_index_location[subbox_index]:
            if v1 in possible_dict[i]:  # update the subbox
                print('🍕', i)
                # possible_dict[i]-{int(str(*v))}
                possible_dict[i].remove(v1)

    def worked_tex_output(self):#output the  worked tex
        self.forced_tex_output() # to get the possible_dict
        self.marked_tex_output() # to get tht marked_sudoku_dict
        self.worked_sudoku_dict = deepcopy(
        self.marked_sudoku_dict)  # copy the marked_sudoku_dict
        worked_possible_dict=self.possible_dict # get the possible_dict
        subbox_location_index=self.subbox_location_index
        row_index_location=self.row_index_location
        column_index_location=self.column_index_location
        subbox_index_location=self.subbox_index_location
        print('⏫',worked_possible_dict)
        print('⚽',row_index_location)
        print('⚾',column_index_location)
        print('🏀',subbox_index_location)
        print(self.worked_sudoku_dict)

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
                            self.worked_sudoku_dict[i][v1]=True # mark cancel

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
                            self.worked_sudoku_dict[i][v1]=True # mark cancel

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
                            self.worked_sudoku_dict[i][v1]=True # mark cancel

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
                if self.worked_sudoku_dict[k1][i]==False: # cancel the rest
                    self.worked_sudoku_dict[k1][i]=True
            possible_dict[k1] = set()  # delete the found number
            # update the line row and subbox
            subbox_index = subbox_location_index[k1]  # get the sub index
            for i in row_index_location[y]:
                if v1 in possible_dict[i]:  # update the row
                    print('🍣', i)
                    # possible_dict[i]-{int(str(*v))}
                    possible_dict[i].remove(v1)
                    self.worked_sudoku_dict[i][v1]=True # mark cancel
            for i in column_index_location[x]:
                if v1 in possible_dict[i]:  # update the column
                    print('🍚', i)
                    # possible_dict[i]-{int(str(*v))}
                    possible_dict[i].remove(v1)
                    self.worked_sudoku_dict[i][v1]=True # mark cancel
            for i in subbox_index_location[subbox_index]:
                if v1 in possible_dict[i]:  # update the subbox
                    print('🍕', i)
                    # possible_dict[i]-{int(str(*v))}
                    possible_dict[i].remove(v1)
                    self.worked_sudoku_dict[i][v1]=True # mark cancel
        
        Temp_worked_sudoku_dict=defaultdict()        
        while(Temp_worked_sudoku_dict!=self.worked_sudoku_dict):
            preemative_pair()
            Temp_worked_sudoku_dict=deepcopy(self.worked_sudoku_dict)
            find_forced_number(worked_possible_dict,self.worked_sudoku_dict)
            
            
        self.tex_output(self.worked_sudoku_dict, '_worked_test') # TODO: DELETE THE _test


# v0.0.1,v0.0.2
# Sudoku('sudoku_wrong_1.txt') # find 80 numbers,there is one missing
# TODO: check where is the missing line.
# Sudoku('sudoku_wrong_2.txt') # !!  missing one line
# Sudoku('sudoku_wrong_3.txt') # SudokuError:incorrect input



# v0.0.3
test = Sudoku('sudoku_1.txt')
test.preassess()  # There is clearly no solution
test = Sudoku('sudoku_2.txt')
test.preassess()  # There is clearly no solution
test = Sudoku('sudoku_3.txt')
test.preassess()  # There might be a solution

# v0.0.5
# TODO: check if use the cancel(True) if still work
test.bare_tex_output()  # out put the sudoku_3_bare.tex

# v0.0.6
# TODO: merge the forced and marked suduku
test.marked_tex_output()
test.forced_tex_output()

# v0.0.7
test1 = Sudoku('sudoku_5.txt')
test1.preassess()
test1.bare_tex_output()
test1.forced_tex_output()
test1.marked_tex_output()

# v0.0.8 # TODO: fix the problem of read the file without space like sudoku_4
test4 = Sudoku('sudoku_4.txt')
test4.preassess()
test4.bare_tex_output()
test4.forced_tex_output()
test4.marked_tex_output()
test4.worked_tex_output()

# v0.0.12 # TODO: test sudoku_5
test5 = Sudoku('sudoku_5.txt')
test5.preassess()
test5.bare_tex_output()
test5.forced_tex_output()
test5.marked_tex_output()
test5.worked_tex_output()

# 
test6 = Sudoku('sudoku6.txt')
test6.preassess()
test6.bare_tex_output()
test6.forced_tex_output()
test6.marked_tex_output()
test6.worked_tex_output()

test7 = Sudoku('sudoku7.txt')
test7.preassess()
test7.bare_tex_output()
test7.forced_tex_output()
test7.marked_tex_output()
test7.worked_tex_output()

