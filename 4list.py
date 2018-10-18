# -*- coding: utf-8 -*-

'''
#4-1
pizzalist = ['fruit', 'durian', 'pepperoni']
for pizza in pizzalist:
	print('I like ', pizza, 'pizza!')
print('I really like pizza!')

#4-2
animals = ['dog', 'cat', 'panda']
for animal in animals:
	print(animal)
for animal in animals:
	print('A', animal, 'would make a great pet')
print('Any of these animals would make a great pet')

#4-3
for n in range(1, 21):
	print(n)

#4-4
for n in range(1, 10000):
	print(n)
t = list(range(1, 10000))

#4-5
print(min(t))
print(max(t))
print(sum(t))

#4-6
t = list(range(1, 21, 2))
for n in t:
	print(n)

#4-7

#t = list(range(3, 31))
#print(t)
t1 = [n for n in range(3, 31) if n % 3 == 0]
for n in t1:
 	print(n)

#4-8
for n1 in [n**3 for n in range(1, 11)]:
	print(n1)

#4-9
t= list(n**3 for n in range(1, 11))


#4-10
animals = ['dog', 'cat', 'panda', 'tiger']
print('The frist three items in the list are:')
print(animals[0:3])
print('Three items from the middle of the list are:')
print(animals[-3:])
'''
#4-11
friend_pizza = ['fruit', 'durian', 'pepperoni']
friend_pizza.append('pineapple')
print(friend_pizza)

#4-12
bufft = ('apple', 'salmon', 'roast duck', 'pork')
print(bufft)
for n in bufft:
	print(n)
