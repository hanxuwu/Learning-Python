# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    return {}
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
import copy
import math
#from collections import defaultdict


# expend the Matrix with Zero
def append_matrix(_grid,_nb_step):
    new_grid=copy.deepcopy(_grid)  # Cope the original Matrix 
    nb_step=_nb_step #number need to append
    nb_line=len(new_grid)  
    for _ in range(nb_step):   # append row first
        new_grid.append(list(0 for _ in range(nb_line)))

    nb_row=len(new_grid) 

    for i in range (nb_row):     # then append line
        for _ in range(nb_step):
            new_grid[i].append(0)
    return new_grid

new_grid=append_matrix(grid,math.ceil(dim/2))   # get the expended matrix


def All_stairs_in_grid():  #  save the position in a dict   [SIZE]:position of the left corner
    count=0
    d=defaultdict(list)
    step=0
    for size in range(2,math.ceil(dim/2)+1):  #size

        count=0   # counter
        for y in range(dim):   
            count=0
            for x in range(dim):

                if new_grid[y][x]==0:  

                    count=0     
                    #continue
                else:
                                               
                    count+=1
                    if count==size:  
   
                        for column in range(0,size):  
                            if new_grid[y+column][x]==0:  
                                count=size-1
                                break
                        else:
                            
                            for line in range(size):   
                                if new_grid[y+size-1][x+line]==0:  # 
                                        count=size-1
                                        break
                                        #continue
                            else:
                                step+=1
                                d[size].append([y+size-1,x])    
                                count=size-1   
      
                    else:
                        pass
        
    return d

All_the_steps=All_stairs_in_grid()

#print('ALL STEP',All_the_steps)
   


#list_1=All_the_steps[2][4]
#print('LIST_1',list_1)
            
            
#print(d)            
#for key,value in d.items():
#for i in range(len(d[2])):
 #   c=list_add(d[2][i],1)
  #  if c in d[2]:
   #     print(d[2][i])
        
        
        
final=[]
new_list=[]
answer=[]


def list_minus(_list,i):  
    new_list=list([(x-y) for x,y in zip(_list,[i,i])])
    return new_list

def list_add(_list,i): 
    new_list=list([(x+y) for x,y in zip(_list,[i,i])])
    return new_list



def count_stairs(d,size):
    answer=[]
    answer_dict=defaultdict(list)
    for i in d[:]:
        count=0
        #print('THIS',i)
        if list_add(i,size-1) in d[:]:
            #print('I',i)
            count+=1
            while((list_add(i,size-1)) in d[:]):
                count+=1
             #   print('IN D',i)
                c=list(list_add(i,size-1))
              #  print(i)
                
                d.remove(i)
                #d = filter(lambda x:xd[i],d)
                i=c     
            #print('BREAK',i)
            answer_dict[count].append(i)
            d.remove(i)
            #print(d)
           # print('CCCCOOOOUUUNNNNTTTT',count)
            #final.append(count)
            continue
    for i in d:
        answer_dict[1].append(i)
    return answer_dict


ED_ANSWER=defaultdict(list)
for size in All_the_steps.keys():
    final=count_stairs(All_the_steps[size],size)
    for step in final.keys():
        #print(step,len(final[step]))
        ED_ANSWER[size].append((step,(len(final[step]))))

        
    
        
            
    
#print(sorted(ED_ANSWER[2]))
#print(ED_ANSWER)    
stairs = ED_ANSWER
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in sorted(stairs[step_size]):
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
