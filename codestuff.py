def q1():
	print('Hello World')

def q2():
	user = input('Enter your name:')
	print('Hello,', user)
def q3():
	n = int(input("Enter preferred number:"))
	sum1 = 0
	while(n > 0):
		sum1 = sum1 + n
		n = n - 1
	print("Calculated sum:", sum1)
def q5():
	n = int(input("Enter preferred number:"))
	pro1 = 1
	while(n > 0):
		pro1 = pro1 * n
		n = n - 1
	print("Calculated product:", pro1)
def q6():
	for i in range(1, 13):
		for j in range(1, 13):
			print(i*j, end='')
			print(' ' * (10-(len(str(i*j)))), end='')
		print('\n')
	
