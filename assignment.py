menu = """
1. Say 'Hello World'
2. Ask your name and greet you.
3. Find the sum from 1 to n.
4. Find the sum from 1 to n that are multiples of 3 or 5.
5. Find the product from 1 to n.
6. Print a multiplication table to 12.
7. Play a guessing game.
8. Exit
"""


while(True):
	print(menu)

	choice = input()

	if choice == '1':
		from codestuff import * 
		q1()
	elif choice == '2':
		from codestuff import *
		q2()
	elif choice == '3':
		from codestuff import *
		q3()
	elif choice == '4':
		from codestuff import *
		q4()
	elif choice == '5':
		from codestuff import *
		q5()
	elif choice == '6':
		from codestuff import *
		q6()
	elif choice == '8':
		break 

