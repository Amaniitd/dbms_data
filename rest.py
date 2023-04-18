
import csv

input_file = 'restaurants.csv'

output_restaurants = 'restaurants-formatted.csv'
output_cuisines = 'cuisines.csv'

f1 = open(input_file, 'r', encoding='utf-8')
f2 = open(output_restaurants, 'w', encoding='utf-8')
f3 = open(output_cuisines, 'w', encoding='utf-8')



id = 0
for line in f1:
   if id == 0:
      rest_line = "id, name, fullAddress, priceRange, zipCode"
      cuis_line = "restaurant_id, cuisine_type"
      f2.write(rest_line)
      f3.write(cuis_line)
   else:
      Line2 = []
      count_quote = 0
      s = ""
      for i in range(len(line)):
         if line[i] == ',':
            if count_quote % 2 == 0:
               Line2.append(s)
               s = ""
            else:
               s += line[i]
         elif line[i] == '"':
            count_quote += 1
            s += line[i]
         else:
            s += line[i]
      Line2.append(s)
      line = Line2
      # rest_line: 0, 2, 7, 6, 8
      # if line have less than 9 items, add empty string
      if len(line) < 9:
         for i in range(9 - len(line)):
            line.append("")
      rest_line = [line[0], line[2], line[7], line[6], line[8]]
      # cuis_line: 0, 5
      cuis_line = [line[0], line[5]]
      # write to restaurants.csv
      s = ""
      for item in rest_line:
         s += item + ","
      s = s[:-1]
      f2.write(s)
      # write to cuisines.csv
      s = ""
      for item in cuis_line:
         s += item + ","
      s = s[:-1]
      f3.write(s)
   id += 1
   f2.write("\n")
   f3.write("\n")
   
   

