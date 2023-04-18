
# user id range: 1-50000
# restaurant id range: 1-40227

import random


ouput_file = 'owner.csv'

f1 = open('owner.csv', 'w', encoding='utf-8')

f1.write('user_id, restaurant_id\n')

random_small_users = random.sample(range(1, 50000), 5000)

for i in range(1, 100000):
   user_id_idx = random.randint(1, 5000)
   user_id = random_small_users[user_id_idx-1]
   restaurant_id = random.randint(1, 40227)
   f1.write(str(user_id) + ',' + str(restaurant_id) + '\n')