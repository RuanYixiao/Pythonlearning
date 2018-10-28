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

prompt = "Please input which one you want to " 
t = True

while t:
	s = input("Please input which one you want to " +
	"add into pizza!" + "\n" +
	" enter 'quit' to quit the program!")
	print('Your pizza will be cooked with %s' % s)

	if s == 'quit':
		t =False

#7-5
s = True
while s:
	age1 = input('Please tell me your age' + 
		"\n enter 'quit' to quit ")

	if age1 == 'quit':
		s = False
		continue

	age = int(age1)

	if age < 3:
		print('You are free')
	elif 3 <= age <= 12:
		print('You should pay 10 dollars!')
	else:
		print('You should pay 15 dollars!')

#7-6
#7-7
#mountain_poll
responses = {}
flag = True

while flag:
	name = input("\n What's your name?")
	mountain = input("\n Which mountain do you" +
		"want to poll")

	responses[name] = mountain
	print("Would you like to let another person" +
		" to respond? yes/no\n")
	repeat = input()

	if repeat == 'no':
		flag = False

print("\n---The result!")

for key, Value in responses.items():
	print('%s likes to climb the %s' % (key, Value))


#7-8
sandwich_order = ['tuna sandwich', 'apple sandwich',
	'turkey sandwich']

finished_sandwiches = []

while sandwich_order:
	sandwich = sandwich_order.pop()
	print('I made ' + sandwich)

	finished_sandwiches.append(sandwich)

print('There are some sandwiches：')
for n in finished_sandwiches:
	print('   ' + n)

#7-9
finished_sandwiches = ['tuna sandwich', 'pastrami sandwich', 'apple sandwich',
	'turkey sandwich', 'pastrami sandwich', 'pastrami sandwich']

print('Sorry to tell that the pastrami sandwich is saled out!')

while 'pastrami sandwich' in finished_sandwiches:
	finished_sandwiches.remove('pastrami sandwich')

for n in finished_sandwiches:
	print('  ' + n)
'''	
def print_model(unprint_models, completed_models):
	
	while unprint_models:
		printing_model = unprint_models.pop()
		completed_models.append(printing_model)

		print("\nThe model in printing is:")
		print('-' + printing_model)


finished_sandwiches = ['tuna sandwich', 'pastrami sandwich', 
	'apple sandwich', 'turkey sandwich', 'pastrami sandwich',
	'pastrami sandwich']
f = []

print_model(finished_sandwiches, f)	
	