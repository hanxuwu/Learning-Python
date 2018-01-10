from itertools import permutations
from collections import defaultdict
from time import time

with open ('wordsEn.txt','rt') as f:
    dictionary=set(f.read().split())

import sys

while True:
    try:
        a=str(input('Enter between 3 and 10 lowercase letters: '))
        s=(a.replace(' ',''))
        for alp in s:
            #print(alp)
            if not alp.islower():
                raise ValueError('Incorrect input, giving up...')
                #break
        if ((len(s)<3)|(len(s)>10)):
            raise ValueError('Incorrect input, giving up...')
            
        #else:
            #raise ValueError('Incorrect input, giving up...')
            
            
        break
    except ValueError:
        print('Incorrect input, giving up...')
        sys.exit()

start=time()
letter=[chr(i) for i in range(97,97+26)]
letter=[chr(x) for x in range(97,97+26)]
letter_value=[2,5,4,4,1,6,5,5,1,7,6,3,5,2,3,5,7,2,1,2,4,6,6,7,5,7]
dict_letter={letter[x]:letter_value[x] for x in range(26)}
dict_letter['\'']=0

dict_letter

count_frq=dict()
sum=0
for i in s:
    if i in count_frq:
        count_frq[i] += 1
    else:
        count_frq[i] = 1
    sum+=dict_letter[i]
    
def check_frq(word):
    check_dict=dict()
    for i in word:
        if i in check_dict:
            check_dict[i] += 1
        else:
            check_dict[i] = 1
    #print(check_dict)
    #print(count_frq)
    for v,k in check_dict.items():
        if v in count_frq.keys():
            if check_dict[v]>count_frq[v]:
                return False
    return True
    
s_score=sum

#print('SCORE %s  %d '%(s,sum))
sum_alpha=0
score_dict=defaultdict(list)
max_sum=0
for i in dictionary:
    sum_alpha=0
    if len(i)<=len(s):
        for alpha in i:
            if alpha in set(s):
                sum_alpha+=dict_letter[alpha]
            else:
                break
            if sum_alpha<=s_score:
                if(check_frq(i)):                    
                    score_dict[sum_alpha].append(i)
                    if sum_alpha>max_sum:
                            max_sum=sum_alpha

final_list=[]
G=set()
E=set()
F=set()
#print(max_sum)
for score in range(max_sum,1,-1):
    if len(final_list)>0:
            break
    for word in score_dict[score]:#score_dict:
        G=set()
        #print(word)
        for wordnumber in range((min(len(s),len(word))),0,-1):
            input_word=set(permutations(s,wordnumber))
            given_word=set(permutations(word,wordnumber))
            #print('WORD',word)
            G=input_word&given_word
            if (G)!=set():
                final_list.append(word)
                break
            else:
                break
    #print(score)
        

#print(max_sum)                
#print('FINAL',final_list)
end=time()
#print('TIMEEE',end-start)
final_score=0
if len(final_list)==0:
    print('No word is built from some of those letters.')
elif len(final_list)==1:
    for i in final_list[0]:
        final_score+=dict_letter[i]
    print(f'The highest score is {final_score}.')
    print(f'The highest scoring word is {final_list[0]}')
else:
    for i in final_list[0]:
        final_score+=dict_letter[i]    
    print(f'The highest score is {final_score}.')
    #is_or_are = 'is' if len(final_list) == 1 else 'are'
    print(f'The highest scoring words are, in alphabetical order:')
    for i in sorted(final_list):
        print('   ',i)
