from math import pi, e

'''
this module provides simple arithmetic operation between two members
type(member) = 'int' or 'float'; 
it is also possible to use main constants from the math module
'''

const = {'pi': pi, 'e': e}
operationList = ['+','-','*','/']


def switch():
	'''
	enables/disables calc.py module itself
	press Enter to proceed
	press 'off' to exit
	'''
	toggle = input("hit 'Enter' to proceed or print 'off' to exit: ")
	if toggle == 'off':
		return False
	else:
		return True

		
def num1():
	#returns first number/constant in expression as 'int' or 'float'
	while True:
		a = input("Enter first number or const: ")
		try:
			a = int(a) 
		except:
			try:
				a = float(a)
			except:
				try:
					a = const[a]
				except:
					print("Error! Please, enter a number or const")
					continue
				else:
					return a
					break
			else:
				return a
				break
		else:
			return a
			break
	

def num2():
	#returns first number/constant in expression as 'int' or 'float'
	while True:
		b = input("Enter second number or const: ")
		try:
			b = int(b) 
		except:
			try:
				b = float(b) 
			except:
				try:
					b = const[b]
				except:
					print("Error! Please, enter a number or const")
					continue
				else:
					return b
					break
			else:
				return b
				break
		else:
			return b
			break
		

def mathOperation():
	#returns operation of the expression, i.e.: (+ or - or * or /) as 'str'
	while True:
		sign = input('Enter an operation: ')
		if sign in operationList:
			return sign
			break
		else:
			print ('Please, enter one of the following: + or - or * or /')
			continue

		
def linkFunction(num1, num2, mathOperation):
	'''
	returns the result of the operation itself, i.e.: result = num1 + num2, etc.
	takes three functions as arguments: (num1, num2, operation)
	'''
	num1 = num1()
	mathOperation = mathOperation()
	num2 = num2()
	if mathOperation == '+':
		result = num1 + num2
		return result
	elif mathOperation == '-':
		result = num1 - num2
		return result
	elif mathOperation == '*':
		result = num1 * num2
		return result
	elif mathOperation == '/':
		result = num1 / num2
		return result
		
		
if __name__ == '__main__':
	while switch():
		answer = linkFunction(num1, num2, mathOperation)
		print('The answer is: {}'.format(answer))