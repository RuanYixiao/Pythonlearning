'''
try:
	with open ('file.txt') as f_obj:
		content232 = f_obj.read()
except FileNotFoundError:
	msg = 'Sorry! the file \'file.txt\' does not exist!'
	print(msg)


#文本分析
title = 'Alice in Wonderland'
print(title.split())
leng = title.split()
print(len(leng))

file_name = 'Alice.txt'

with open (file_name) as f:
	cover_letter = f.read()

cover_words = cover_letter.split()
print(len(cover_words))

with open (file_name, 'w') as f1:
	f1.write('I Love ZhaoNannan！')
	f1.write("very much!")

with open (file_name, 'a') as f:
	f.write('I want to marry ZhaoNannan！')

def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open (filename) as f:
			content0 = f.read()
	except FileNotFoundError:
		print('Sorry, the file ' + filename + ' does not exist')
	else:
		words = content0.split()
		num = len(words)
		print('the file ' + filename + ' has about ' + str(num) +
			' words !')

file_name = 'Alice.txt'
count_words(file_name)

files = ['Alice.txt', 'pi_digits.txt', 'iiii.txt']

for file in files:
	count_words(file)

#数据储存
import json

number = [1, 2, 3, 4, 5]

with open ('numbers.json', 'w') as f:
	json.dump(number, f)

file_name = 'numbers.json'

with open (file_name) as f:
	a = json.load(f)
print(a)

username = input('Please input your name ')

file_name = 'username.json'
with open (file_name, 'w') as f:
	json.dump(username, f)
	print("We'll remember you when you come back " + username + "!")

with open (file_name) as f:
	print(json.load(f)) 

'''

import json

file_name = 'username.json'


def got_username():
	try:
		with open (file_name) as f:
			username = json.load(f)
	except FileNotFoundError:
		None
	else:
		return username

def get_newuser():
	username = input("What's your name? ")

	with open(file_name, 'w') as f:
		json.dump(username, f)
	return username

def greet():
	username = got_username()

	if username:
		print("Welcome, " + username)
	else:
		username = get_newuser()
		print("We'll remember you When you come back" + username)

greet()
'''		
try:
	with open (file_name) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What's your name? ")

	with open (file_name, 'w') as f:
		json.dump(username, f)
	print("We'll remember you When you come back" + username)
else:
	print("Welcome back, " + username)
'''