# -*- coding: utf-8 -*-
'''
alien_0 = {'color' : 'grren', 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#6-1
nannan = {
	'Frist_name' : 'Zhao',
	'Last_name' : 'nannan',
	'age' : 18,
	'city' : 'tongliao',
	}
print(nannan)

#6-2
Lovenumber = {
	'zhaonannan' : 8,
	'ruanyixiao' : 5,
	'liuyuling' : 4,
	'ruanqifneg' : 2,
	}

print(Lovenumber)

#6-3
wordlist = {
	'sum' : 'the sum of all numbers',
	'max' : 'the maximum number of all numbers',
	'min' : 'the minimum numbers of all numbers',
	}
print('The mean of sum: \n' + wordlist['sum'])



#6-4
for key, value in wordlist.items():
	print(key)

#6-5
rivers = {
	'Nile River' : 'Egypt',
	'Changjiang River' : 'China',
	'Amazon River' : 'Brazli',
	'Mississippi River' : 'USA'
	}

for river, cuntry in rivers.items():
	print('The %s runs through %s' % (river, cuntry))

for river in rivers.keys():
	print(river)
for cuntry in rivers.values():
	print(cuntry)

#6-6
favorite_languages = {
	'jen' : 'Python',
	'sarah' : 'C',
	'edward' : 'Ruby',
	'phi' : 'Python',
	}

person_list = [
	'jen', 
	'sarah', 
	'edward', 
	'phi', 
	'zhaonannan',
	]

for person in person_list:
	if person in favorite_languages.keys():
		print(person + ', Thankes you for coming')
	else:
		print(person + 
			', Please tell me your favorite language')


#6-7
nannan = {
	'Frist_name' : 'Zhao',
	'Last_name' : 'nannan',
	'age' : 18,
	'city' : 'tongliao',
	}
ruanyixiao = {
	'Frist_name' : 'Ruan',
	'Last_name' : 'Yixiao',
	'age' : 18,
	'city' : 'Chongqing',
	}
YansShidong = {
	'Frist_name' : 'Yan',
	'Last_name' : 'Shidong',
	'age' : 18,
	'city' : 'Suzhou',
	}

people = [nannan, ruanyixiao, YansShidong]

for peoples in people:
	print(people)
'''
# 6-8

#6-9
favorite_places = {
	'zhaonannan' : ['Dandong', 'Shenyang', 'Chongqing'],
	'ruanyixiao' : ['Jingshan', 'Chongqing', 'Shenyang'],
	'YansShidong' : ['Jingzhou', 'Chongqing', "Suzhou"],
	}

for person in favorite_places.items():
	print(person)