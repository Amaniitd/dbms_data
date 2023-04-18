
# user id range: 1-50000
# restaurant id range: 1-40227
# rating range: 1-5

import random


ouput_file = 'ratings.csv'
f2 = open(ouput_file, 'w', encoding='utf-8')

f2.write('id, user_id, restaurant_id, total_rating, food_rating, service_rating, ambience_rating\n')

for i in range(1, 100000):
   user_id = random.randint(1, 50000)
   restaurant_id = random.randint(1, 40227)
   food_rating = random.randint(1, 5)
   service_rating = random.randint(1, 5)
   ambience_rating = random.randint(1, 5)
   total_rating = (food_rating + service_rating + ambience_rating) // 3
   review = 'review' + str(i)
   f2.write(str(i) + ',' + str(user_id) + ',' + str(restaurant_id) + ',' + str(total_rating) + ',' + str(food_rating) + ',' + str(service_rating) + ',' + str(ambience_rating) + '\n')
