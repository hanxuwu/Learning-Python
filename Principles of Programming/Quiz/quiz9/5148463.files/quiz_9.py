# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M, and
# - when leaves in T are expanded to 2 leaves in T*, those 2 leaves receive the same value.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    all_path=[]
    track=[]
    sum_list=[]
    def traversal_path(tree):
        #print(tree.value)
        if tree is not None:
            track.append(tree.value)
            if tree.left_node is None and tree.right_node is None:
                #print(track[:])
                sum_list.append(sum(track[:-1]))
                all_path.append(track[:-1])
            traversal_path(tree.left_node)
            traversal_path(tree.right_node)
            track.pop() 

    position=[]
    value=[]
    a=[]
    b=[]
    path_list=[]
    def modify_path(tree):
        if tree is not None:
            track.append(tree.value)
            path_list.append(tree)
            if tree.left_node is None and tree.right_node is None:
                #print(path_list[-2].value)
                #print('@',max_number-sum(track[:-1]))
                a.append(path_list[-2])
                b.append(max_number-sum(track[:-1]))
            modify_path(tree.left_node)
            modify_path(tree.right_node)
            #print(path_list[-1].value)
            track.pop() 
            path_list.pop()
    traversal_path(tree)
    max_number=max(sum_list)
    modify_path(tree)
    for i in range(len(a)):
        #print(a[i].value,b[i])
        if b[i]==0:
            continue
        if a[i].left_node.value is None:
            #print('#',a[i].value)
            a[i].left_node=BinaryTree(b[i])
            continue
        if a[i].right_node.value is None:
            #print('@',a[i].value)
            a[i].right_node=BinaryTree(b[i])
    # Replace pass above with your code


# Possibly define other functions

                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()



