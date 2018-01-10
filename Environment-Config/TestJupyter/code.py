grid=[[3,3,0,2,4,3],
        [3,2,3,2,4,1],
        [4,1,2,1,0,4],
        [2,4,4,1,2,0],
        [0,2,3,4,0,2],
        [3,2,4,1,4,3]]

# 3 3 0 2 4 3
# 3 2 3 2 4 1
# 4 1 2 1 0 4
# 2 4 4 1 2 0
# 0 2 3 4 0 2
# 3 2 4 1 4 3


matrix=list(grid)

max_length=4
height=6
width=6


for i in matrix:
    print(*i,end='')
    print()
    
print('@@',matrix)

# Append the 0 around the matrix
def expend_matrix(matrix):
    matrix.insert(0,list([0 for _ in range(width)]))
    matrix.append(list([0 for _ in range(width)]))
    for i in matrix:
        i.insert(0,0)
        i.append(0)
    return matrix


def recur_number(y,x,L):
    L_point=list(L)
    for i in range(4):
        if matrix[y-1][x]+1==matrix[y][x]:
            L_point.append((y,x))
            return recur_number(y-1,x,L)
        elif matrix[y][x+1]+1==matrix[y][x]:
            L_point.append((y,x))
            return recur_number(y,x+1,L)
        elif matrix[y+1][x]+1==matrix[y][x]:
            L_point.append((y,x))
            return recur_number(y+1,x,L)
        elif matrix[y][x-1]+1==matrix[y][x]:
            L_point.append((y,x))
            return recur_number(y,x-1,L)
        matrix[y][x]=-1
        ps=L_point.pop()
        return recur_number(ps[0],ps[1],L)
        
        
            
        #matrix[y][x]
for row_index,row in enumerate(matrix):
    for line_index,line in enumerate(matrix[row_index]):
        print('Y',row_index)
        #print(row)
        #print('X',line_index)
        #print(line)
        
expend_matrix(matrix)