
import json
output_file = 'user.csv'
f1 = open(output_file, 'w', encoding='utf-8')

s = "id,name,email,password\n"
f1.write(s)

id = 1
with open('data.json') as f:
   data = json.load(f)
   for item in data:
      s = str(id) + "," + item['name'] + "," + item['email'] + "," + item['password'] + "\n"
      f1.write(s)
      id += 1



