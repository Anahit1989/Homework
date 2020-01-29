def maximum_number():
	if number1<=number2<=number3 or number2<=number1<=number3:
		return number3
	elif number1<=number3<=number2 or number3<=number1<=number2:
		return number2
	else:
		return number1
number1=int(input("Please enter the first number: "))
number2=int(input("Please enter the second number: "))
number3=int(input("Please enter the third number: "))
print(maximum_number())

def fizz_buzz(number):
	if number%3==0 and number%5:
		return "Fizz"
	elif number%3 and number%5==0:
		return "Buzz"
	elif number%3==0 and number%5==0:
		return "FizzBuzz"
	else:
		return number
number=int(input("Please enter an arbitrary number: "))
print(fizz_buzz(number))

def show_numbers(limit):
	if i%2:
		return i, "ODD"
	else:
		return i, "EVEN"
limit=int(input("Please enter an arbitrary number: "))
for i in range(0,limit):
	print(show_numbers(limit))

def compute_number():
	return n+11*n+111*n
n=int(input("Please enter an arbitrary number: "))
print(compute_number())

def x(n):
	return n**2+1

n=int(input("Please enter an arbitrary number: "))
print(x(n))