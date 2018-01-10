# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2014
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


# Written by Eric Martin for COMP9021


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
    if top_n <= 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

year_1 = min(years)
year_2 = max(years)
year_1_index = 4 + year_1 - 1960
year_2_index = 4 + year_2 - 1960
relative_increases = defaultdict(list)
with open(agricultural_land_filename, encoding = 'utf-8') as agricultural_land_csvfile,\
                                        open(forest_filename, encoding = 'utf-8') as forest_csvfile:
    data = zip(csv.reader(agricultural_land_csvfile), csv.reader(forest_csvfile))
    for _ in range(5):
        next(data)
    for agricultural_land_data, forest_data in data:
        try:
            agricultural_land_area_1 = float(agricultural_land_data[year_1_index])
            agricultural_land_area_2 = float(agricultural_land_data[year_2_index])
            forest_area_1 = float(forest_data[year_1_index])
            forest_area_2 = float(forest_data[year_2_index])
            if agricultural_land_area_2 - agricultural_land_area_1 <= 0 or\
                                                                 forest_area_2 - forest_area_1 <= 0:
                continue
            proportion = (agricultural_land_area_2 - agricultural_land_area_1) /\
                                                                     (forest_area_2 - forest_area_1)
        except ValueError:
            continue
        relative_increases[proportion].append(agricultural_land_data[0])
countries = [''.join((country, ' (', f'{proportion:.2f}', ')'))
                                        for proportion in sorted(relative_increases, reverse = True)
                                                       for country in relative_increases[proportion]
            ]
countries = countries[: top_n]

print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    
