# Insert your code here
while True:
    try:
        N = int(input('Enter the desired goal cell number: '))
        if N <= 0 :
            raise ValueError('Incorrect value, try again')
        break
    except ValueError:
        print('Incorrect value, try again')

def Direction_generator():
    sum1=2
    temp=5
    Direction=[]
    for i in range(0,1000):
        sum1+=8*i
        for ri in range(sum1-2*i-1,sum1):
            Direction.append('right')
        for do in range(sum1,sum1+2*i+1):
            Direction.append('down')
        for le in range(sum1+2*i+1,sum1+2*i+1+2*(i+1)):
            Direction.append('left')
        temp=sum1+8*(i+1)
        for up in range(sum1+2*i+1+2*(i+1),temp-2*(i+1)-1):
            Direction.append('up')
            
        #print(Direction)
    return Direction
    


def Pivoting_die(instruction_list,goal_cell_number):
    
    def right_rule(L):
        right,front,bottom,top,left,back=L[0],L[1],L[2],L[3],L[4],L[5]  
        L[0],L[1],L[2],L[3],L[4],L[5]=top,front,right,left,bottom,back
        return L
    
    def down_rule(L):
        front,bottom,right,left,back,top,=L[0],L[1],L[2],L[3],L[4],L[5]
        L[0],L[1],L[2],L[3],L[4],L[5]=top,front,right,left,bottom,back
        return L
    
    def left_rule(L):
        left,front,top,bottom,right,back=L[0],L[1],L[2],L[3],L[4],L[5]
        L[0],L[1],L[2],L[3],L[4],L[5]=top,front,right,left,bottom,back
        return L
    
    def up_rule(L):
        back,top,right,left,front,bottom=L[0],L[1],L[2],L[3],L[4],L[5]
        L[0],L[1],L[2],L[3],L[4],L[5]=top,front,right,left,bottom,back
        return L

    dice_dict={1:6,2:5,3:4,4:3,5:2,6:1}
    dice_rule={'right':right_rule,'down':down_rule,'left':left_rule,'up':up_rule}
    top=3
    bottom=4
    front=2
    back=5
    right=1
    left=6
    temp=0
    Dice_list = [top,front,right,left,bottom,back] #top,front,right,left,bottom,back
    if goal_cell_number==0:
        return Dice_list
    else:
        for i in range(goal_cell_number):
                dice_rule[instruction_list[i]](Dice_list)
            
        return Dice_list
instruction_list=Direction_generator()
final=Pivoting_die(instruction_list,N-1)
print('On cell %d, %d is at the top, %d at the front, and %d on the right.'%(N,final[0],final[1],final[2]))
#print(instruction_list)
