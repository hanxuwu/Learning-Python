# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *
from copy import deepcopy



# Possibly define some functions
    
def preferred_sequence():
    temp_list = []

    def delete(subclass, i):  # delete the assign number then bubble down
        if subclass.is_empty():
            raise EmptyPriorityQueueError(
                'Cannot delete element from empty priority queue')
        max_element = subclass._data[i]
        subclass._data[i], subclass._data[subclass._length] = subclass._data[subclass._length], subclass._data[i]
        subclass._length -= 1
        subclass._bubble_down(i)
        return max_element
    for index, i in enumerate(pq._data[1: len(pq) + 1]):
        temp_list.append((i, index + 1))

    for i in sorted(temp_list)[::-1]:
        a, b = i

    final_list=[]
    
    for time in range(length):
        temp_max=0
        temp_index=-1
        
        for i in range(1, len(pq) + 1):
            temp_pq = deepcopy(pq)

            before_delete=temp_pq._data[: len(temp_pq) + 1]
            delete_number=delete(temp_pq, i)

            temp_pq.insert(delete_number)
            after_delete=temp_pq._data[: len(temp_pq) + 1]


            if before_delete==after_delete:

                if delete_number> temp_max:
                    temp_max=delete_number
                    temp_index=i
        

        final_list.append(temp_max)
        delete(pq, temp_index)

    return final_list[::-1]
    # Replace pass above with your code (altogether, aim for around 24 lines of code)


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())

