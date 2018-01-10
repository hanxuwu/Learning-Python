# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Replace this comment with your code
# Hanxu Wu  z5148463    
import math
def Arrange_middle(L):
    M_f =[]
    Middle_index=math.floor(len(L)/2)
    if len(L)<=1:
        return L
    else:
        M_f.append(L[Middle_index])
        if len(L)%2 ==0:   
            for index in range(Middle_index):
                M_f.append(L[index])
                M_f.append(L[-(index+1)])
            M_f.pop()
        else:
             for index in range(Middle_index):
                M_f.append(L[index])
                M_f.append(L[-(index+1)])
    return M_f
#-------------------------------------------------------------
from collections import OrderedDict

def Generate_order(L):
        d = OrderedDict()
        for index in range(len(L)):
            d[index]=L[index]   
        N_f=[]
        Check_exist=set()
        index = 0
        while(len(Check_exist)!=len(L)):
            if index not in Check_exist:     
                N_f.append(d[index])
                Check_exist.add(index)
                index = d[index]
            else:
                for b in range(len(L)):
                    if b not in Check_exist:
                        index = b
                        break
        return N_f
#--------------------------------------------
M=Arrange_middle(L)
N=Generate_order(L)
    
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
