# create a program to reduce entries randomly from a csv file
# and write them to a new csv file

percent = 0.1 # percent of entries to keep
input_file = 'restaurant-menus.csv'
output_file = 'restaurant-menus-reduced.csv'

import random

f1 = open(input_file, 'r', encoding='utf-8')
f2 = open(output_file, 'w', encoding='utf-8')

id = 0
for line in f1:
   if (id == 0):
      f2.write(line)
      id += 1
   else: 
      if random.random() <= percent:
            f2.write(line)

         
