# -*- coding: utf-8 -*-
'''
#7-1
car = input('What\'s car do you want?')
print("Let's see if I can find a %s" % car)

#7-2
person_of_eating = input("How many people will" +
	" come to have dinner?" + "\n")
person_of_eating1 = int(person_of_eating)

if person_of_eating1 > 8:
	print('There has no empty table!')
else:
	print('There has a empty table')


#7-3
number_int = input('Please input a number!' + '\n')
number = int(number_int)
if number % 10 == 0:
	print('Yes')
else:
	print('no')

#7-4
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 != 0:
		continue  

	print(current_number)
'''
prompt = "Please input which one you want to " 
t = True

while t:
	s = input("Please input which one you want to " +
	"add into pizza!" + "\n" +
	" enter 'quit' to quit the program!")
	print('Your pizza will be cooked with %s' % s)

	if s == 'quit':
		t =False
	
	