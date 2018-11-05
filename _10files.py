# -*- coding: utf-8 -*-

with open (r'C:\Users\ysd15\Documents\GitHub\Pythonlearning\pi_digits.txt') as f:
	contents1 = f
	print(contents1.read())

file_path = r'C:\Users\ysd15\Documents\GitHub\Pythonlearning\pi_digits.txt'

with open (file_path) as f:
	print(f.read())

with open ('pi_digits.txt') as f:
	for line in f:
		print(line)

with open ('pi_digits.txt') as f:
	lines = f.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))


#异常
try:
	print(5 / 0)
except ZeroDivisionError as e:
	print('You can\'t divide by zero!')

print(" Give me two numbers, and I'll divide them!")
print("Enter 'q' to quit!")

while True:
	first_number = input("First number: ")
	if first_number == "q":
		break

	second_number = input("Second_number: ")
	if second_number == "q":
		break

	try:
		answer = int(first_number) / int(second_number)
		print(answer)
	except ZeroDivisionError:
		print('You can not divide by 0!')
	else:
		print(answer)

while True:
	first_number = input("The first number is:")
	if first_number == "q":
		break
	second_number = input('The second number is:')
	if second_number == 'q':
		break

	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print('You can not divide by 0')
	else:
		print('the answer is:')
		print(answer)


