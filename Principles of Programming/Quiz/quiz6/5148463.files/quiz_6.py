# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by *** and Eric Martin for COMP9021


from collections import defaultdict

class PermutationError(Exception):
    def __init__(self, message):
        self.message = message
        #print(self.message)
        

class Permutation:
    def __init__(self, *args, length = None):
        self.sum1=0    
        self.L=args
        self.length=length
        self.nb_of_cycles=0
        self.s=''
#############################################################################################
        
        if not self.L and self.length:
            self.L=tuple(range(1,self.length+1))
        #try:
        for i in self.L:
            self.sum1+=1
            if not isinstance(i,int):
                raise PermutationError('Cannot generate permutation from these arguments')
            if i==0:
                raise PermutationError('Cannot generate permutation from these arguments')
        if self.length:
            if self.sum1!=self.length:
                raise PermutationError('Cannot generate permutation from these arguments') 
        #except PermutationError:
            #print(None)
################################################################################            
        a=self.L
        L=[]
        d=dict()
        index1=[]
        value1=[]
        for index,t in enumerate(a):
            L.append((index+1,t))
            index1.append(index+1)
            value1.append(t)
            d[index+1]=t

        d=defaultdict(list)
        search_flag=False  #search Flag
        for i in L[:]:   
            if not L:   # finish condition
                    break
            if search_flag==False:   # new search
                current,lookfor=L[0]
                d[current].append(lookfor)
            flag=False
            for t in L[1:]:   
                search_flag=True
                x,y=t
                if x==lookfor:   #find it
                    flag=True
                    d[current].append(y)
                    if not y==current:   # if not  loop
                        lookfor=y
                        L.remove(t)
                    else:            # if loop 
                        L.remove(t)
                        search_flag=False
                        L.remove(L[0])
                        break
            if not flag:   #didnt find 
                search_flag=False
                L.remove(L[0])
        final=dict()
        for v in d.values():
            max_v=max(v)
            index_maxv=v.index(max_v)
            final[max_v]=v[index_maxv:]+v[:index_maxv]
        for k in sorted(final):
            self.nb_of_cycles+=1
            self.s=self.s+'('+' '.join(list(map(str,final[k])))+')'  
        # Replace pass above with your code
########################################################################################
    def __len__(self):
        return self.sum1
        # Replace pass above with your code
        
    def __repr__(self):
        return 'Permutation'+str(self.L)
        # Replace pass above with your code
        
    def __str__(self):
        if not self.s:
            self.s='()'
        return  self.s
    
    def __mul__(self, permutation):
        list1=(self.L)
        list2=(permutation.L)
        d_mul=defaultdict(list)
        #try:
        if not self.__len__()==permutation.__len__():
            raise PermutationError('Cannot compose permutations of different lengths')
        #except PermutationError as e:
            #pass
            #sys.exit()
            
        for index1,value1 in enumerate(list1):
            d_mul[value1].append(index1+1)
        for index2,value2 in enumerate(list2):
            d_mul[index2+1].append(value2)
        return Permutation(*list(i[1] for i in sorted(d_mul.values(),key=lambda x:x[0])))

    def __imul__(self, permutation):
        return self.__mul__(permutation)
        
        
        # Replace pass above with your code

    def inverse(self):
        #print('Before',self.L)
        inv_L=self.L[:]
        inv_L=list(inv_L)
        new_list=[]
        for ind,num in enumerate(inv_L):
            new_list.append((ind+1,num))
        return Permutation(*list(i[0] for i in sorted(new_list,key=lambda x:x[1])))
        
    # Insert your code for helper functions, if needed



                
                    
        
