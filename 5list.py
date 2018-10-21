# -*- coding: utf-8 -*-

cars = ['honda', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

if 'Glee' not in cars:
	print('Glee is great!')
'''
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
'''

#5-5


