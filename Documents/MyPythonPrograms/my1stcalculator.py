# Defining Functions

name = raw_input("Hello, What is your name?")
print "welcome %s" %name, "Enjoy Using!!"

def add(x, y):
	return x + y
def subtract(x, y):
	return x - y
def multiply(x, y):
	return x * y
def devide(x, y):
	return x / y

# Take input from the user
print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = raw_input("Enter Choice (1/2/3/4):")
num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: "))

if choice == "1":
	print(num1, "+",num2, "=", add(num1,num2))
elif choice == "2":
	print(num1, "-", num2, "=", subtract(num1,num2))
elif choice == "3":
	print(num1, "*",num2,"=", multiply(num1,num2))
elif choice == "4":
	print(num1,"/", num2,"=", divide(num1,num2))
else:
	print("Read the rules, Massa!")




# import operatorModule

# operator_module.add(3, 2)




# from operator_module import add 

# #Luis 22

# print("SIMPLE CALCULATOR! ")
# print('Please enter an integer value:')
# x = input()

# print('Please enter another integer value:')

# y = input()

# num1 = int(x)

# num2 = int(y)

# print(num1, '+', num2, '=', num1 + num2)

# print(num1, '*', num2, '=', num1 * num2)

# print(num1, '/', num2, '=', num1 / num2)

# print(num1, '-', num2, '=', num1 - num2)