class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: {}".format(self.restaurant_name))
        print("The cuisine type is: {}".format(self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant {} is now open!! :D".format(self.restaurant_name))

restaurant = Restaurant("Tacos de grasa","Mexicana")
print(restaurant.restaurant_name, ",", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
