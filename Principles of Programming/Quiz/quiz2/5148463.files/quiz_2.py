# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# Replace this comment with your code
from collections import defaultdict
from fractions import Fraction


fraction_list=[]
def fraction_generate(L):
    
    if len(L)==0:
        print('I failed to generate one strictly positive number, giving up.')
    for a in range(len(L)):
        for b in range(a,len(L)):
                if(L[a]==L[b]):
                    if L[b]!=0:
                        fraction_list.append(Fraction(L[a],L[b]))
                    else:
                        pass
                elif L[a]<L[b]:
                    if L[b]!=0:
                        fraction_list.append(Fraction(L[a],L[b]))
                    else:
                        pass
                else:
                    if L[a]!=0:
                        fraction_list.append(Fraction(L[b],L[a]))
                    else:
                        pass
    return fraction_list



## Sort the key
def Generate_Dict(F):
    d=defaultdict(set)
    for i in range(len(F)):
        temp_key = F[i]-Fraction(1,2)
        d[temp_key].add(F[i])
        temp_key=0
    #print('Orginal Dict\n',d)
    return d

#def Generate_Dict(F):
 #   for i in range(len(F)):
  #      temp_key = F[i]-Fraction(1,2)
   #     dict_d={temp_key:F[i]}
    #return dict_d



def Sort_Dict_Key(t):
    key=set()
    sorted_key=[]
    sorted_fraction=[]
    for i in t.keys():
        key.add(i)
    sorted_key=sorted(key)
   # print('sorted_key\n',sorted_key)
    #for i in range(len(sorted_key)):
        #sorted_fraction.append(t[sorted_key[i]])
    return sorted_key

def Generate_abs_Dict(F):
    for_return=[]
    List_minus_1_2=[]
    d=defaultdict(set)
    min_abs=Fraction(1)
    for i in range(len(F)):
        #List_minus_1_2.append(abs(F[i]))
        
        temp_key = Fraction(abs(F[i]))
        #print('TEMP',temp_key)
        #print(type(temp_key))
        if temp_key<min_abs:
            #print(min_abs)
            min_abs=Fraction(temp_key)
        else:
            min_abs=Fraction(min_abs)
         #   print('MIN',min_abs)
        d[temp_key].add(F[i]+Fraction(1,2))
        #d[temp_key].add(0)
        #print('TEMP TWO',temp_key)
        #print('Dict',d)

        #temp_key=0

    for_return=[str(i) for i in d[min_abs]]

    return for_return

#start=time()

Fraction_lowest_term=fraction_generate(L)
#start_Generate_Dict=time()

t=Generate_Dict(Fraction_lowest_term)
#end_Generate_Dict_time=time()

t1=dict(t)

list_sorted =Sort_Dict_Key(t1)
list_sorted_1=list(list_sorted)

#end_list_sorted=time()

fractions=[str(i+Fraction(1,2)) for i in list_sorted]
#end_fractions=time()

fractions_1=[(i) for i in list_sorted_1]

#end_fractions_1=time()

#print('fraction1',fractions_1)

List_closest_2=Generate_abs_Dict(fractions_1)



if len(List_closest_2)==1:
    if List_closest_2[0]=='1/2':
        spot_on=True        
    else: closest_1=List_closest_2[0]
elif len(List_closest_2)==2:
    closest_1, closest_2=List_closest_2[0],List_closest_2[1]

print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

