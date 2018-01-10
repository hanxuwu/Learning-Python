from collections import deque
import sys

while True:
	try:
		a=str(input('Input final configuration: '))
		N=int(a.replace(' ',''))
		if ((N>87654321)|(N<12345678)):
			raise ValueError('Incorrect configuration, giving up...')
		break
	except ValueError:
		print('Incorrect configuration, giving up...')
		sys.exit()
		

final=[int(i) for i in str(N)]

    

def initial_state(N):
    initial_list = []
    for i in range(1, N + 1):
        locals()['d' + str(i)] = i
        name_list = [('d' + '%d' % i) for i in range(1, N + 1)]
    for i in range(N):
        initial_list.append(vars()[name_list[i]])
    return initial_list


def row_exchange(L):
    r_L = list(L)
    d8, d7, d6, d5, d4, d3, d2, d1 = r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7]
    r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7] = d1, d2, d3, d4, d5, d6, d7, d8
    return r_L


def right_circular_shift(L):
    r_L = list(L)
    d1, d2, d3, d4, d5, d6, d7, d8 = r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7]
    r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7] = d4, d1, d2, d3, d6, d7, d8, d5
    return r_L


def middle_clockwise_rotation(L):
    r_L = list(L)
    d1, d2, d3, d4, d5, d6, d7, d8 = r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7]
    r_L[0], r_L[1], r_L[2], r_L[3], r_L[4], r_L[5], r_L[6], r_L[7] = d1, d7, d2, d4, d5, d3, d6, d8
    return r_L

def Rubik_Rectangle(initial_list, final_conf_list):
    steps_need = 0
    created_list = list(initial_list)
    check_list = []
    created_total = []
    created_all=deque()
    created_all.append([1, 2, 3, 4, 5, 6, 7, 8])    
    temp_created_all=[]
    Flag = False
    temp_created_all=[]
    temp_created_all.append([1, 2, 3, 4, 5, 6, 7, 8])
    
    don_t_know=set()
    don_t_know.add((1, 2, 3, 4, 5, 6, 7, 8))
    
    
    def List_compare(list_1, list_2, i):
        if list_1 == list_2:
            return True
        else:
            return False

    for i in range(23):
        #print('I',i)
        #print('LENTH OF ALL',len(created_all))
        steps_need = i
        if initial_list == final_conf_list:
            return steps_need
        else:
                for element in range(0, len(created_all)):
                    created_list = created_all[element]
                    if tuple(row_exchange(created_list)) not in don_t_know:
                        created_total.append(row_exchange(created_list))
                        check_list = row_exchange(created_list)
                        Flag = List_compare(check_list, final_conf_list, steps_need)
                        if Flag == True:
                            #print(check_list)
                            return steps_need + 1
                for element in range(0, len(created_all)):
                    created_list = created_all[element]
                    if tuple(right_circular_shift(created_list)) not in don_t_know:
                        created_total.append(right_circular_shift(created_list))
                        check_list = right_circular_shift(created_list)
                        Flag = List_compare(check_list, final_conf_list, steps_need)
                        if Flag == True:
                            #print(check_list)
                            return steps_need + 1
                for element in range(0, len(created_all)):
                    created_list = created_all[element]
                    if tuple(middle_clockwise_rotation(created_list)) not in don_t_know:
                        created_total.append(middle_clockwise_rotation(created_list))
                        check_list = middle_clockwise_rotation(created_list)
                        Flag = List_compare(check_list, final_conf_list, steps_need)
                        if Flag == True:
                            #print(check_list)
                            return steps_need + 1
                #print('------------------------------------------')
                #bug 
                bug_L=[1,3,7,14,26,51,92,159,274,453,720,1115,1727,2603,3701,4729,5620,6240,5840,4492,2120,328,5,0]
                
                created_all1=deque(maxlen=bug_L[steps_need+1])

                for i in range(len(created_total)):
                     if tuple(created_total[i]) not in don_t_know:
                        created_all1.append(created_total[i])
                        don_t_know.add(tuple(created_total[i]))
                temp_created_all=list(created_all1) 

                created_all=list(created_all1)

                for num in range(len(created_all)):
                    check_list = created_all[num]
                    Flag = List_compare(check_list, final_conf_list, steps_need)
                    if Flag == True:
                        #print(check_list)
                        return steps_need + 1
                created_total = list()
                
initial_list=[1,2,3,4,5,6,7,8]
#final = [1,5,3,2,4,6,7,8]


#print('step',Rubik_Rectangle(initial_list, final))
nb_of_stairs=Rubik_Rectangle(initial_list, final)
stair_or_stairs = 'step is' if nb_of_stairs <= 1 else 'steps are'

print(f'{nb_of_stairs} {stair_or_stairs} needed to reach the final configuration.')

