
import json
output_file = 'user.csv'
f1 = open(output_file, 'w', encoding='utf-8')

s = "id,name,email,password\n"
f1.write(s)

def clean(s):
   # make password alphanumeric
   s2 = ""
   for c in s:
      if c.isalnum():
         s2 += c
   return s2

id = 1
with open('data.json') as f:
   data = json.load(f)
   for item in data:
      pwd = clean(item['password'])
      s = str(id) + "," + item['name'] + "," + item['email'] + "," + pwd + "\n"
      f1.write(s)
      id += 1



