# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by Eric Martin for COMP9021

import sys
from random import seed, sample

from priority_queue_adt import *


def _preferred_sequence(pq, data, length):
    if length == 1:
        return [data[0]]
    for e in data:
        current_pos = length
        while current_pos and pq[current_pos] < e:
            if current_pos == 1:
                break
            sibling_pos = current_pos + 2 * (1 - current_pos % 2) - 1
            if sibling_pos < length and pq[current_pos] < pq[sibling_pos]:
                break
            current_pos //= 2
        else:
            current_pos = length
            current_datum = pq[current_pos]
            while current_pos and current_datum < e:
                parent_datum = pq[current_pos // 2]
                pq[current_pos // 2] = current_datum
                current_datum = parent_datum
                current_pos //= 2
            data.remove(e)
            return _preferred_sequence(pq, data, length - 1) + [e]
       
def preferred_sequence():
    data = sorted(pq._data[1: len(pq) + 1], reverse = True)
    return _preferred_sequence(pq._data[: len(pq) + 1], data, length)


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

