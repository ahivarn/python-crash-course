# ~ class Dog:
	# ~ """A simple attempt to model a dog."""
	# ~ def __init__(self, name, age):
		# ~ """Initializa name and age attributes."""
		# ~ self.name = name
		# ~ self.age = age
	
	# ~ def sit(self):
		# ~ """Simulate a dog sitting in response to a command!"""
		# ~ print(f"{self.name} is now sitting.")

	# ~ def roll(self):
		# ~ """Simulate a roll over"""
		# ~ print(f"{self.name} has rolled over.")
		
# ~ mydog = Dog('Willie', 6)
# ~ print(f"My dog's name is {mydog.name.title()}.")
# ~ print(f"My dog is {mydog.age} years old.")

# ~ mydog.sit()
# ~ mydog.roll()
# ~ your_dog = Dog('Lucy', 3)

# ~ print(f"My dog's name is {mydog.name.title()}.")
# ~ print(f"My dog is {mydog.age} years old.")
# ~ mydog.sit()
# ~ print(f"\n")
# ~ print(f"Your dog's name is {your_dog.name.title()}.")
# ~ print(f"Your dog is {your_dog.age} years old.")
# ~ your_dog.sit()

#Exercise 9-1 , 9-2
# ~ class Restaurant:
	# ~ def __init__(self, restaurant_name, cuisine_type):
		# ~ self.restaurant_name = restaurant_name
		# ~ self.cuisine_type = cuisine_type
	
	# ~ def describe_restaurant(self):
		# ~ print(f"The name of restaurant is {self.restaurant_name.title()}.")
		# ~ print(f"They provide {self.cuisine_type.title()} food here.\n")

	# ~ def open_restaurant(self):
		# ~ print(f"The restaurant {self.restaurant_name.title()} is now open.")


# ~ restaurant1 = Restaurant('Swiggy', 'indian')
# ~ print(restaurant1.restaurant_name)
# ~ print(restaurant1.cuisine_type)
# ~ restaurant1.describe_restaurant()
# ~ restaurant1.open_restaurant()

# ~ restaurant2 = Restaurant('zOmato', 'desi')
# ~ restaurant3 = Restaurant('kfc', 'fried chicken')
# ~ restaurant2.describe_restaurant()
# ~ restaurant3.describe_restaurant()


##Ex 9-3
# ~ class Users:
	# ~ def __init__(self, first_name, last_name, age, location, gender):
		# ~ self.first_name = first_name.title()
		# ~ self.last_name = last_name.title()
		# ~ self.age = age
		# ~ self.location = location.title()
		# ~ self.gender = gender.title()
	# ~ def describe_user(self):
		# ~ print(f"{self.first_name} {self.last_name}")
		# ~ print(f"\t-of {self.gender} gender.")
		# ~ print(f"\t-Age is {self.age}.")
		# ~ print(f"\t-Lives in {self.location}.\n")
	# ~ def greet_user(self):
		# ~ print(f"Welcome, {self.first_name}")
		
# ~ wife = Users('miilee', 'baby', 27, 'mumbai', 'female')
# ~ wife.greet_user()
# ~ wife.describe_user()

# ~ mummy = Users('shila', 'devi', 54, 'nawada', 'female')
# ~ mummy.greet_user()
# ~ mummy.describe_user()

# ~ papa = Users('shri surya', 'prakash', 58, 'nawada', 'male')
# ~ papa.greet_user()
# ~ papa.describe_user()


#Exercise 9-4
# ~ class Restaurant:
	# ~ def __init__(self, restaurant_name, cuisine_type,number_served=0):
		# ~ self.restaurant_name = restaurant_name
		# ~ self.cuisine_type = cuisine_type
		# ~ self.number_served = number_served
	
	# ~ def describe_restaurant(self):
		# ~ print(f"The name of restaurant is {self.restaurant_name.title()}.")
		# ~ print(f"They provide {self.cuisine_type.title()} food here.\n")

	# ~ def open_restaurant(self):
		# ~ print(f"The restaurant {self.restaurant_name.title()} is now open.")
		
	# ~ def set_no_served(self, served):
		# ~ self.number_served = served
	
	# ~ def increment_no_served(self, addition_no):
		# ~ self.number_served += addition_no

# ~ manpasand = Restaurant('manpasand', 'indian')
# ~ manpasand.describe_restaurant()

# ~ manpasand = Restaurant('manpasand', 'indian',10)
# ~ manpasand.describe_restaurant()
# ~ print(manpasand.number_served)
# ~ manpasand.set_no_served(50)
# ~ print(manpasand.number_served)
# ~ manpasand.increment_no_served(30)
# ~ print(manpasand.number_served)

##Ex 9-5
# ~ class Users:
	# ~ def __init__(self, first_name, last_name, age, location, gender,\
# ~ login_attempts=0):
		# ~ self.first_name = first_name.title()
		# ~ self.last_name = last_name.title()
		# ~ self.age = age
		# ~ self.location = location.title()
		# ~ self.gender = gender.title()
		# ~ self.login_attempts = login_attempts
	# ~ def describe_user(self):
		# ~ print(f"{self.first_name} {self.last_name}")
		# ~ print(f"\t-of {self.gender} gender.")
		# ~ print(f"\t-Age is {self.age}.")
		# ~ print(f"\t-Lives in {self.location}.")
		# ~ print(f"\t-You attempted logins {self.login_attempts} times.\n")
	# ~ def greet_user(self):
		# ~ print(f"Welcome, {self.first_name}")
	# ~ def increment_login_attempts(self):
		# ~ self.login_attempts += 1
	# ~ def reset_login_attempts(self):
		# ~ self.login_attempts = 0
		
# ~ wife = Users('miilee', 'baby', 27, 'mumbai', 'female')
# ~ wife.greet_user()
# ~ wife.describe_user()

# ~ mummy = Users('shila', 'devi', 54, 'nawada', 'female')
# ~ mummy.greet_user()
# ~ mummy.describe_user()

# ~ papa = Users('shri surya', 'prakash', 58, 'nawada', 'male')
# ~ papa.greet_user()
# ~ papa.describe_user()
# ~ papa.increment_login_attempts()
# ~ papa.increment_login_attempts()
# ~ papa.describe_user()
# ~ papa.increment_login_attempts()
# ~ papa.describe_user()
# ~ papa.reset_login_attempts()
# ~ papa.describe_user()

# ~ class Car:
	# ~ """A simple model to represent a car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ self.make = make
		# ~ self.model = model
		# ~ self.year = year 
		# ~ self.odometer_reading = 0
		
	# ~ def get_descriptive_name(self):
		# ~ long_name = f"{self.year} {self.make} {self.model}"
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ print(f"This car has {self.odometer_reading} miles on it.")
		
	# ~ def update_odometer(self, mileage):
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		# ~ else:
			# ~ print(f"You can't roll back an odometer!'")

	# ~ def increment_odometer(self, miles):
		# ~ self.odometer_reading += miles

# ~ class ElectricCar(Car):
	# ~ """Represent aspects of a car, specific to electric vehicles."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize the attributes of the parent class."""
		# ~ super().__init__(make, model, year)
		# ~ """Atrributes specific to electric cars"""
		# ~ self.battery_size = 76
		
	# ~ def describe_battery(self):
		# ~ """Print a statement descrbing battery size"""
		# ~ print(f"This car has a {self.battery_size}-kWh battery.")

	# ~ def fill_gas_tank(self):
		# ~ """Electric cars dont have gas tanks!"""
		# ~ print(f"This car doesnt need a gas tank!")
# ~ my_tesla = ElectricCar('tesla', 'model s', 2019)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.describe_battery()
# ~ my_tesla.fill_gas_tank()



###Instances as Attributes
# ~ class Car:
	# ~ """A simple model to represent a car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ self.make = make
		# ~ self.model = model
		# ~ self.year = year 
		# ~ self.odometer_reading = 0
		
	# ~ def get_descriptive_name(self):
		# ~ long_name = f"{self.year} {self.make} {self.model}"
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ print(f"This car has {self.odometer_reading} miles on it.")
		
	# ~ def update_odometer(self, mileage):
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		# ~ else:
			# ~ print(f"You can't roll back an odometer!'")

	# ~ def increment_odometer(self, miles):
		# ~ self.odometer_reading += miles

# ~ class Battery:
	# ~ """A simple attempt to model a battery for an Electric car"""
	# ~ def __init__(self, battery_size=75):
		# ~ self.battery_size = battery_size
		
	# ~ def describe_battery(self):
		# ~ """Print a statement describing battery size."""
		# ~ print(f"This car has a {self.battery_size}-kWh battery.")
		
	# ~ def get_range(self):
		# ~ """print battery range"""
		# ~ if self.battery_size <=75:
			# ~ range = 100
		# ~ elif self.battery_size>=100:
			# ~ range = 200
		# ~ else:
			# ~ range = 150
		# ~ print(f"This car can go {range} miles on a full charge.")
		
# ~ class ElectricCar(Car):
	# ~ """Represent aspects of a car, specific to electric vehicles."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize the attributes of the parent class."""
		# ~ super().__init__(make, model, year)
		# ~ """Atrributes specific to electric cars"""
		# ~ self.battery = Battery()

# ~ my_tesla = ElectricCar('tesla', 'model s', 2019)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.battery_size = 55
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()

#Exercise 9-4
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type,number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
	
	def describe_restaurant(self):
		print(f"The name of restaurant is {self.restaurant_name.title()}.")
		print(f"They provide {self.cuisine_type.title()} food here.\n")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name.title()} is now open.")
		
	def set_no_served(self, served):
		self.number_served = served
	
	def increment_no_served(self, addition_no):
		self.number_served += addition_no

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name, cuisine_type, number_served):
		super().__init__(restaurant_name, cuisine_type, number_served)
		self.flavors = []
	def show_flavors(self):
		print(f"\nThe icecream stand {self.restaurant_name.title()} has following flavors: ")
		for flavor in self.flavors:
			print(f"\t-{flavor.title()}")

manpasand = Restaurant('manpasand', 'indian')
manpasand.describe_restaurant()

manpasand = Restaurant('manpasand', 'indian',10)
manpasand.describe_restaurant()
print(manpasand.number_served)
manpasand.set_no_served(50)
print(manpasand.number_served)
manpasand.increment_no_served(30)
print(manpasand.number_served)

naturals = IceCreamStand('naturals', 'healthy icecream', 50)
naturals.flavors = ['butterscoch', 'vanilla','mango', 'tutti-frutti']
naturals.show_flavors()





























































