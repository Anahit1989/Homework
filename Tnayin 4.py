memory=input("Please enter a childhood memory of yours: ")
print("The fact that memory is a sentence is:"," " in memory)
print("The fact that memory is a word is: "," " not in memory)
number1=input("Please enter an arbitrary number: ")
number1=int(number1)
x=number1%5
print("The fact that number1 cann't be divied to 5 is: ", bool(x))
number2=input("Please enter an arbitrary number: ")
number2=int(number2)
y=number2%11
print("The fact that number2 cann't be divied to 11 is: ", bool(y))
number3=input("Please enter an arbitrary number: ")
number3=int(number3)
z=number3%5*11
print("The fact that number3 cann't be divied to both 5 and 11 is: ", bool(z))
days_in_year=input("Enter the numbers of days in any year: ")
days_in_year=int(days_in_year)
d=days_in_year%2
print("The fact that the year is not a leap year is: ", bool(d))