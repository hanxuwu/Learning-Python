# Written by Eric Martin for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if not self.head:
            return
        node = self.head
        if self.head.value % 2:
            while node.next_node and node.next_node.value % 2:
                node = node.next_node
            if not node.next_node:
                return
            odd_tail = node
            even_tail = node.next_node
            even_head = even_tail
            node = node.next_node
            odd_tail.next_node = None
        else:
            while node.next_node and not node.next_node.value % 2:
                node = node.next_node
            if not node.next_node:
                return
            even_tail = node
            odd_tail = node.next_node
            even_head = self.head
            self.head = odd_tail
            node = node.next_node
            even_tail.next_node = None           
        while node.next_node:
            if node.next_node.value % 2:
                odd_tail.next_node = node.next_node
                odd_tail = odd_tail.next_node
            else:
                even_tail.next_node = node.next_node
                even_tail = even_tail.next_node
            node = node.next_node
        odd_tail.next_node = even_head       
        even_tail.next_node = None        
    
    
