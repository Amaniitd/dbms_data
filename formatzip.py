input_file = 'zip.csv'
output_file = 'zip-formatted.csv'

f1 = open(input_file, 'r', encoding='utf-8')
f2 = open(output_file, 'w', encoding='utf-8')


id = 0

for line in f1:
   if id == 0:
      # split the line into a list of sings
      line = line.split(',')
      l2 = ["id"]
      for i in range(len(line)):
         if (i == len (line) - 1):
            l2.append(line[i][:-1])
         else:
            l2.append(line[i])
      l2.append("country\n")
      s = ""
      for item in l2:
         s += item + ","
      s = s[:-1]
      print(s)
      f2.write(s)
   else:
      line = line.split(',')
      l2 = [str(id)]
      for i in range(len(line)):
         if (i == len (line) - 1):
            l2.append(line[i][:-1])
         else:
            l2.append(line[i])
      l2.append("US\n")
      s = ""
      for item in l2:
         s += item + ","
      s = s[:-1]
      f2.write(s)
   id += 1
