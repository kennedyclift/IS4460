# This is a single line comment!

#Python Literals

#This is an object of type string
print('Darth') 
#This is a number technically a float
print(4.3)

#Variable Naming Rules
A = 4
a = 2

print(A)
print(a)

#Python Variables
user_name = "Darth"
gpa = 4.3

print(user_name)
print(gpa)

#String Concatenation
print("My name is " + user_name + " not Kylo Ren")

#String Concatenation
print(f"My name is {user_name} not Kylo Ren")

#Variable Typing
number = 11111 * 66666
print(str(number)[1:3])
#use str() to convert the number to a string and use [1:3] to get the first 3 numbers

#Functions
def add_numbers(a,b):
    output = a + b
    return output

print(add_numbers(2,3)) #positional arguments
print(add_numbers(b=8,a=4)) #named arguments

#Variable Scope
name = "Spongebob"

def say_hello():
    name = "Patrick"
    return f"Hello {name}"
print(say_hello())





