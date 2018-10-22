# -*- coding: utf-8 -*-
'''
cars = ['honda', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

if 'Glee' not in cars:
	print('Glee is great!')

#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

#5-2
print('False' == 'True')
print('False1' == 'false1')
t = 'False1 '
print('false1' == t.lower())
print(18 > 17)
print(18 >= 17)
print(13 != 17)

print(18 != 17 or 18 >= 19)
print('toyota' in cars)
print('glee' not in cars)

#5-3
alien_color = 'green'
if alien_color == 'green':
	print('Your got five point!')

#5-4
alien_color = 'green'
if alien_color == 'green':
	print('You got five points')
if alien_color == 'yellow':
	print('You got ten points')

alien_color = 'red'
if alien_color == 'yellow':
	print('You got five points!')
elif alien_color == 'red':
	print('You got fifteen points!')
else:
	print('You got ten points!')


#5-5
alien_color = 'bule'

if alien_color == 'bule':
	print('You got 5 points!')
elif alien_color == 'green':
	print('You got 10 points!')
elif alien_color == 'red':
	print('You got 15 points!')

#5-6
age = 5
if age < 2:
	print('You are a baby!')
elif 2 <= age < 4:
	print('You are learning walk!')
elif 4 <= age < 13:
	print('You are a child!')
elif 13 <= age < 20:
	print('You are a young man!')
elif 20 < age <= 65:
	print('You are an adult!')
elif age > 65:
	print('You are a old man!')

#5-7
favoritr_fruits = ['Apple', 'orange', 'lemon']
if 'Apple' in favoritr_fruits:
	print('You really like Apple!')


#5-8
name_list = ['john', 'bob', 'arics', 'admin']

for name in name_list:
	if name == 'john':
		print('Welcome, jhon!')
	elif name == 'bob':
		print('Welcome, bob!')
	elif name == 'arics':
		print('Welcome, arics!')
	elif name == 'admin':
		print('Hello, admin, would you like to see status report?')
	else:
		print('Hello Eric, thank you for logging in again!')

#5-9
name_list = ['john', 'bob', 'arics', 'admin']
while name_list:
	name_list.pop()
	print(name_list)
	
if name_list == []:
	print('We need to find some users1')

#5-10
current_users = ['Jhon', 'bob', 'arics', 'admin', 'nannan']
new_users = ['jhon', 'ruanyixiao', 'Crv', 'civic', 'admin']
current_users_xiaoxie = []
for name_current_users in current_users:
	current_users_xiaoxie.append(name_current_users.lower())
print(current_users)
print(current_users_xiaoxie)

for name in new_users:
	name_xiao = name.lower()
	if name in current_users_xiaoxie:
		print('Please input another name!')
	else:
		print('This name was not used!')
'''

#5-11
numbers = list(range(1, 10))
for number in numbers:
	print(number)

number_th = []
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(str(number) + 'th')

