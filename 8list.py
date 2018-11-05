# -*- coding: utf-8 -*-
'''
#8-1
def display():
	print('This chapter teaches hhhh')

display()

#8-2
def favorite_books(title):
	print('Your favorite book is \"' + title + '\"')

favorite_books('Walking on the cloud')

#8-3
def make_shirt(number, words):
	print('Your shirt is ' + '\"' + number + '\"' + " ")
	print(words + ' will be on the shirt')

make_shirt('XS', 'Yes')

#8-4
def make_shirt(number = 'L', words = 'I Love Python'):
	print('Your shirt is ' + '\"' + number + '\"' + " ")
	print(words + ' will be on the shirt')

make_shirt()
make_shirt(number = 'M')
make_shirt(words = 'I Love Nannan')

#8-5


#8-6
import sys
sys.path.append('C:/Users/ysd15/Documents/GitHub/Pythonlearning')

from _7list import print_model

models = ['iPhone', 'Xiaomi', 'Huawei']
f = []

print_model(models, f)

def city_country(city, country):
	f = {}
	f[city] = country
	print(f)
	for n, m in f.items():
		print("\"" + city + ", " + country + "\"")

city_country('Santiago', 'Chile')

#8-7
def make_album():
	albums = {}
	print('\nPlease enter the singer\'s name' +
		'and the album\'s name')
	print("enter 'q' to quit!")
	t = True
	while t:
		singer = input("The singer's name is ")
		if singer == "q":
			break
		album = input("The album's nameis ")
		if album == "q":
			break
		albums[singer] = album
	
	return albums
print(make_album())
'''


def make_album1(singer, album, t, number = ''):
	t['singer'] = singer
	t['name'] = album
	if number:
		t['number_songs'] = number
	return t

f = {}
print(make_album1('Andy Lua', 'Say I Love You Again', 
		f, 8))
