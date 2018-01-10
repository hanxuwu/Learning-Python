# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        odd_head=self.head
        even_tail=None
        odd_tail=None
        if not self.head:
            return
        
        
        if self.head.value&1==1:
            if not odd_head.next_node:
                return
            while (odd_head.next_node.value&1==1): #looking for the first even number.     if the next one is odd number
                odd_head=odd_head.next_node # current_pointer move to the next
                if not odd_head.next_node: # if there is no even number at the end,return
                        return
            odd_tail=odd_head #current_pointer is the end of the odd number
            even_head=odd_head.next_node# the first even number is after the current pointer  
            even_tail=even_head #the first even number is also the end of the even number
            odd_tail.next_node=even_head #connect the last odd number with the first even number
            odd_head=odd_head.next_node # the current_pointer move to the next
            
            while(odd_head.next_node): # if there is number after the current pointer,keep looking for
                while (odd_head.next_node.value&1!=1): # if the next one is odd number 
                    odd_head=odd_head.next_node # current_pointer move to the next
                    if not odd_head.next_node: # if there is no even number at the end,return
                        return
                if odd_head.next_node.value &1!=1: #if the number you found is odd number
                    return
                even_tail=odd_head   # the current pointer is the end of the even number
                odd_head=odd_head.next_node #the odd number is after the current pointer
                even_tail.next_node=odd_head.next_node #connect the even tail to the unsearched node
                odd_head.next_node=odd_tail.next_node  #odd_tail.next_node == even_head  connect the odd_tail with even_head
                odd_tail.next_node=odd_head # connect the end odd number to the founded odd number
                odd_tail=odd_head  # the founded odd number became the new odd end
                odd_head=even_tail    # move the current pointer to the node before the unsearched Node 
        else:
            if not odd_head.next_node:
                return
            while (odd_head.next_node.value&1!=1):  #looking for the first odd number.     if the next one is odd number
                odd_head=odd_head.next_node # current_pointer move to the next
                if not odd_head.next_node: # if there is no even number at the end,return
                        return
            even_tail=odd_head #current_pointer is the end of the even number
            odd_head=odd_head.next_node # the first odd number is after the current pointer  
            even_tail.next_node=odd_head.next_node  #connect the even tail to the unsearched node
            odd_head.next_node=self.head # connect the odd head to the even head ,because self head is the even head 
            self.head=odd_head # linkedlist head is the fist odd number
            odd_head=even_tail #the current pointer is the end of the even number
            odd_tail=self.head # for the head,the first found odd number is also the end of the odd number

            while(odd_head.next_node):  # if there is number after the current pointer,keep looking for
                while (odd_head.next_node.value&1!=1):  # if the next one is odd number 
                    odd_head=odd_head.next_node # current_pointer move to the next
                    if not odd_head.next_node: # if there is no even number at the end,return
                        return
                if odd_head.next_node.value &1!=1:  #if the number you found is odd number
                    return 
                even_tail=odd_head  # the current pointer is the end of the even number
                odd_head=odd_head.next_node  #the odd number is after the current pointer
                even_tail.next_node=odd_head.next_node  #connect the even tail to the unsearched node
                odd_head.next_node=odd_tail.next_node #odd_tail.next_node == even_head  connect the odd_tail with even_head
                odd_tail.next_node=odd_head # connect the end odd number to the founded odd number
                odd_tail=odd_head  # the founded odd number became the new odd end
                odd_head=even_tail# move the current pointer to the node before the unsearched Node 
        # Replace pass above with your code
        # Replace pass above with your code
    
    
    
