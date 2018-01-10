#from random import seed
from random import randint
from collections import Counter


def play():
    def generate_poker_dice(nb_dice):
    
        dice_card=['Ace','King','Queen','Jack','10','9']
        poker_dice_dict={i:dice_card[i] for i in range(6)}
        poker_dice_reverse_dict={dice_card[i]:i for i in range(6)}
        random_nunmber=[randint(0,5) for i in range(nb_dice)]
        d=sorted(random_nunmber)
        sorted_roll=[poker_dice_dict[i] for i in d]
        return sorted_roll

    def poker_dice_result(_generated_roll):
        if _generated_roll:        
            counter_list=list(Counter(_generated_roll).values())
            if ((max(counter_list)==2)&(counter_list.count(2)==1)):
                print('It is a One pair')
            elif ((max(counter_list)==2)&(counter_list.count(2)==2)):
                print('It is a Two pair')
            elif ((max(counter_list)==3)&(min(counter_list)==1)):
                print('It is a Three of a kind')
            elif ((max(counter_list)==3)&(min(counter_list)==2)):
                print('It is a Full house')
            elif ((max(counter_list)==4)):
                print('It is a Four of a kind')
            elif ((max(counter_list)==5)):
                print('It is a Five of a kind')
            elif (generated_roll==['Ace', 'King', 'Queen', 'Jack', '10'])|(generated_roll==['King', 'Queen', 'Jack', '10', '9']):
                print('It is a Straight')
            else:
                print('It is a Bust')
        #else:
            #print('Ok, done')
        

        
    def keep_for_the_second(_keep_roll,last):
        dice_card=['Ace','King','Queen','Jack','10','9']
        poker_dice_reverse_dict={dice_card[i]:i for i in range(6)} 
        if (_keep_roll[0]=='All')|(_keep_roll[0]=='all'):
            number_need=0
            return False
        elif (_keep_roll[0]=='none'):
            number_need=5
            new_generated_roll=generate_poker_dice(number_need)
            return sorted(list((Counter(new_generated_roll)).elements()),key=lambda k:poker_dice_reverse_dict[k])
        elif sorted(_keep_roll,key=lambda k:poker_dice_reverse_dict[k])==last:
            return False
            
        
        else:
            keep_counter=Counter(_keep_roll)
            number_need=5-len(_keep_roll)
        new_generated_roll=generate_poker_dice(number_need)
        return sorted(list((keep_counter+Counter(new_generated_roll)).elements()),key=lambda k:poker_dice_reverse_dict[k])
          
    def keep_second_input():
        d=list()
        while True:
            counter_ge=Counter(generated_roll)
            try:
                a=str(input('Which dice do you want to keep for the second roll? '))
                s=list(a.split(' '))
                #print(s)
                for word in s:
                    if ((word=='All')|(word=='all')):
                        return ['All']
                    elif (word==''):
                        return ['none']
                    elif not word in generated_roll:
                        raise ValueError('That is not possible, try again!')
                    else:
                        #print(counter_ge)
                        counter_ge[word]-=1
                        #print(counter_ge)
                d=list(counter_ge.values())
                for i in d:
                    if i<0:
                        raise ValueError('That is not possible, try again!')
                return s
                break
            except ValueError:
                print('That is not possible, try again!')
            
    def keep_third_input():
        d=list()
        while True:
            counter_ge=Counter(second_roll)
            try:
                a=str(input('Which dice do you want to keep for the third roll? '))
                s=list(a.split(' '))
                #print(s)
                for word in s:
                    if ((word=='All')|(word=='all')):
                        return ['All']
                    elif (word==''):
                        return ['none']

                    elif not word in second_roll:
                        raise ValueError('That is not possible, try again!')
                    else:
                        #print(counter_ge)
                        counter_ge[word]-=1
                        #print(counter_ge)
                d=list(counter_ge.values())
                for i in d:
                    if i<0:
                        raise ValueError('That is not possible, try again!')
                return s
                break
            except ValueError:
                print('That is not possible, try again!')

    generated_roll=generate_poker_dice(5)
    print(f'The roll is:',(' '.join([str(i) for i in generated_roll])))
    #print(generated_roll)
    poker_dice_result(generated_roll)
    keep_roll=keep_second_input()
    #print('KEEP',keep_roll)
    second_roll=keep_for_the_second(keep_roll,generated_roll)
    if second_roll:
        print(f'The roll is:',(' '.join([str(i) for i in second_roll])))
        poker_dice_result(second_roll)
        keep_roll=keep_third_input()
        third_roll=keep_for_the_second(keep_roll,second_roll)
        if third_roll:
            print(f'The roll is:',(' '.join([str(i) for i in third_roll])))
        else:
            print('Ok, done.')
        poker_dice_result(third_roll)
    else:
        print('Ok, done.')



def simulate(times):
    simulate_dict=dict()
    one_pair=0
    two_pair=0
    three_kind=0
    full_house=0
    four_kind=0
    five_kind=0
    Stright=0
    def generate_poker_dice(nb_dice):
    
        dice_card=['Ace','King','Queen','Jack','10','9']
        poker_dice_dict={i:dice_card[i] for i in range(6)}
        poker_dice_reverse_dict={dice_card[i]:i for i in range(6)}
        random_nunmber=[randint(0,5) for i in range(nb_dice)]
        d=sorted(random_nunmber)
        sorted_roll=[poker_dice_dict[i] for i in d]
        return sorted_roll
    
    for _ in range(times):
        generated_roll=generate_poker_dice(5)
        #print(generated_roll)
        if generated_roll:        
            counter_list=list(Counter(generated_roll).values())
            #print(counter_list)
            if ((max(counter_list)==2)&(counter_list.count(2)==1)):
                one_pair+=1
                #print('one_pair')
            elif ((max(counter_list)==2)&(counter_list.count(2)==2)):
                two_pair+=1
                #print('two_pair')
            elif ((max(counter_list)==3)&(min(counter_list)==1)):
                three_kind+=1
                #print('three_kind')
                
            elif ((max(counter_list)==3)&(min(counter_list)==2)):
                full_house+=1
                #print('full_house')
                
            elif ((max(counter_list)==4)):
                four_kind+=1
                #print('four_kind')
            elif ((max(counter_list)==5)):
                five_kind+=1
                #print('five_kind')
                
            elif (generated_roll==['Ace', 'King', 'Queen', 'Jack', '10'])|(generated_roll==['King', 'Queen', 'Jack', '10', '9']):
                Stright+=1
                #print('Stright')
    #times=five_kind+four_kind+full_house+Stright+three_kind+two_pair+one_pair            
    print('Five of a kind : %.2f%%'%((five_kind/times)*100))
    print('Four of a kind : %.2f%%'%((four_kind/times)*100))
    print('Full house     : %.2f%%'%((full_house/times)*100))
    print('Straight       : %.2f%%'%((Stright/times)*100))
    print('Three of a kind: %.2f%%'%((three_kind/times)*100))
    print('Two pair       : %.2f%%'%((two_pair/times)*100))
    print('One pair       : %.2f%%'%((one_pair/times)*100))

    
    #return one_pair,two_pair,three_kind,full_house,four_kind,five_kind,Stright

    
    


#play()
#simulate(times)

