# -*- coding: utf-8 -*-

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

#5