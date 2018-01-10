# Written by Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains 1/2, then the fact that 1/2 belongs to "fractions";
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

L = set(L)
includes_0 = 0 in L
if includes_0:
    L.remove(0)
L = sorted(L)
numerators_denominators = set()
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        the_gcd = gcd(L[i], L[j])
        numerators_denominators.add((L[i] // the_gcd, L[j] // the_gcd))
numerators_denominators = [e for e in sorted(numerators_denominators, key = lambda x: x[0] / x[1])]
fractions = [f'{e[0]}/{e[1]}' for e in numerators_denominators]
if includes_0:
    fractions.insert(0, '0')
fractions.append('1')
if not numerators_denominators:
    if not includes_0:
        closest_1 = '1'
    else:
        closest_1, closest_2 = '0', '1'
elif (1, 2) in numerators_denominators:
    spot_on = True
elif numerators_denominators[0][0] * 2 > numerators_denominators[0][1]:
    closest_1 = f'{numerators_denominators[0][0]}/{numerators_denominators[0][1]}'
elif numerators_denominators[-1][0] * 2 < numerators_denominators[-1][1]:
    closest_1 = f'{numerators_denominators[-1][0]}/{numerators_denominators[-1][1]}'
else:
    closest_1 = numerators_denominators[0]
    for i in range(1, len(numerators_denominators)):
        if numerators_denominators[i][0] * 2 > numerators_denominators[i][1]:
            break
    a, b = numerators_denominators[i - 1]
    c, d = numerators_denominators[i]
    x, y = (b - 2 * a) * 2 * d, (2 * c - d) * 2 * b
    if x < y:
        closest_1 = f'{a}/{b}'
    elif x > y:
        closest_1 = f'{c}/{d}'        
    else:
        closest_1, closest_2 = f'{a}/{b}', f'{c}/{d}'


print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
