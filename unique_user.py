
filename = 'user.csv'
f1 = open(filename, 'r', encoding='utf-8')

dict = {}

id = 0
for line in f1:
   if (id == 0):
      id += 1
   else:
      line = line.split(',')
      email = line[2]
      password = line[3]
      ep = email + password
      if ep in dict:
         print("duplicate found")
      else:
         dict[ep] = 1

print("done")
      