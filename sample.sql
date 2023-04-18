
Table Restaurant {
   id int
   name varchar(255)
   fullAddress varchar(255)
   priceRange varchar(255)
   zipCode varchar(255)
}

Table Dish {
   restaurant_id int
   name varchar(255)
   price int
   category varchar(255)
   description varchar(255)
}


Table Address {
   zipCode varchar(255)
   city varchar(255)
   state varchar(255)
   country varchar(255)
}

Table Cuisines {
   restaurant_id int
   cuisine_type varchar(255)
}

Table Rating {
   id int
   user_id int
   restaurant_id int
   total_rating int
   food_rating int
   service_rating int
   ambience_rating int
   review varchar(255)
   
}

Table User {
   id int
   name varchar(255)
   email varchar(255)
   password varchar(255)
}

Table Owner {
    user_id int
   restaurant_id int
}

Ref: Restaurant.id < Dish.restaurant_id
Ref: Restaurant.zipCode > Address.zipCode
Ref: Restaurant.id < Cuisines.restaurant_id
Ref: Rating.user_id > User.id
Ref: Owner.restaurant_id <> Restaurant.id
Ref: Owner.user_id - User.id
Ref: Rating.restaurant_id > Restaurant.id