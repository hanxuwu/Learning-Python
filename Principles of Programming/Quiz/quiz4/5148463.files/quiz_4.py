# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

# Insert your code here
year_1=years.pop()
year_2=years.pop()




from collections import defaultdict

def read_agri_csv(fn=agricultural_land_filename):
    
    with open(fn,encoding='utf-8') as agri:
        csv_agri=csv.reader(agri)        
        for row in csv_agri:
            rows = [row for row in csv_agri][3:]
    return rows

def read_fore_csv(fn=forest_filename):
    
    with open(fn,encoding='utf-8') as agri:
        csv_fore=csv.reader(agri)        
        for row in csv_fore:
            rows = [row for row in csv_fore][3:]
    return rows
            


#year_1=2000
#year_2=2005
#gap=year_2-year_1


def generate_agri_fore_dict(year_1,year_2):
    all_agri=read_agri_csv()
    all_fore=read_fore_csv()
    agri_fore_data=defaultdict(list)
    
    
    
    year1_index=all_agri[0].index(str(year_1))
    year2_index=all_agri[0].index(str(year_2))
    
    for line in all_agri[1:]:        
        if (line[year1_index]!='')&(line[year2_index]!=''):
            if (float(line[year2_index])-float(line[year1_index])>0):
                agri_fore_data[line[0]].append((float(line[year2_index])-float(line[year1_index])))
            else: 
                continue
        else:
            continue
            
    for line in all_fore[1:]:
        if (line[year1_index]!='')&(line[year2_index]!=''):
            if (float(line[year2_index])-float(line[year1_index])>0):
                agri_fore_data[line[0]].append((float(line[year2_index])-float(line[year1_index])))
            else: 
                continue
        else:
            continue
    return agri_fore_data





agri_fore_dict=generate_agri_fore_dict(year_1,year_2)
agri_fore_dict

final_dict=defaultdict(list)
for k,v in agri_fore_dict.items():
    #print(k,v)
    if len(v)==2:
        final_dict[(v[0])/(v[1])].append(k)
        

dict_key=sorted(final_dict.keys(),reverse=True)

formatkey=list(['%.2f'%a for a in dict_key])

#print('FOR',formatkey)



#for i in range(4):
#    print(final_dict[dict_key[i]],dict_key[i])
    

            
#country=['china','japan','korea']
#rate=[155.7143,45.0,5654.90]


countries=[]
for i in range(top_n):
    countries.append(final_dict[dict_key[i]][0]+' '+'('+str(formatkey[i])+')')



print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    
