# -*- coding: utf-8 -*-
'''
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, age, name):
		self.age, self.name = age, name

	def sit(self):
		print(self.name + 'is sitting')

	def roll_over(self):
		print(self.name + 'is rolling over')\

	def get_name(self):
		print("The dog is " + self.name)

my_dog = Dog(6, "Elles")
my_dog.get_name()

class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def descriptive_name(self):
		"""返回简介的描述信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("The car has " + str(self.odometer_reading) + 
			" miles on it")
	def update_odometer(self, mileage):
		"""将里程表读数设置为制定值"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			#print('You can\'t roll back an odmeter')



my_car = Car('audi', "A4", 2014)
print(my_car.descriptive_name())
my_car.read_odometer()

my_car.update_odometer(67)
my_car.read_odometer()

class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery('Toshiba')


class Battery(object):
	"""docstring for Battery"""
	def __init__(self, battery_name, battery_size = 70):
		self.battery_name = battery_name
		self.battery_size = battery_size

	def get_battery_name(self):
		print("This car uses " + self.battery_name)

	def get_battery_size(self):
		print("This car has a " + str(self.battery_size) + 
			"-kWh battery")

	
my_tesla = ElectricCar('tesla', 'model S', 2017)
print(my_tesla.descriptive_name())

my_tesla.battery.get_battery_size()

my_tesla.battery.get_battery_name()

print(my_tesla.year)

with open ('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

'''
