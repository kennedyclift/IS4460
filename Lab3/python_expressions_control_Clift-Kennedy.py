#Python Boolean
print(f"e: {20 < 24}")
print(f"f: {6 == 6}")
print(f"g: {1 == 0}")
print(f"h: {1 == 1}")

#Python Boolean Contd
print("Is one equal to 2:",int(1 == 2))
print("Is one equal to 1:",int(1 == 1))

#Literals and Variables
myname = "Kennedy"
myage = 21

print(f"a: {12}") #This is a numeric literal
print(f"b: {'Hello'}") #This is a string literal
print(f"c: {False}") #This is a constant literal
print(f"d: {myname}") #This is a string variable
print(f"e: {myage}") #This is a numeric variable

#Precedence
print((1 - 2 + 2),(2 - 2 +1))
print((1 * 2 + 4),(4 * 2 +1))

#Relational Operators
print(f"Is 'chewbacca'=='chewy'? {'chewbacca'=='chewy'}")

#Equality Operators
my_name = "Harry Potter"
print("Assignment: ",my_name)
print("Equality: ",my_name == "Harry Potter")

#Comparison Operators
print ("Comparison - bb is less than c:", "bb" < "c")
print("Comparison - 7 is less than 10:", 7 < 10)

#IF  Statement
bank_balance = 500
savings = 700
if bank_balance < 700:
    money = 2000
    bank_balance += money
elif bank_balance > 300:
    savings += 100
    bank_balance -+ 60
else:
    savings += 500
    bank_balance -= 500
    print("Balance is less than or equal to 500.")
print(bank_balance)
print(savings)

#The Ternary Operator
fuel = 500
print("Fill the tank sometime today" if fuel >= 306 else "There's enough fuel for today")

#While Loop
fuel = 98
while fuel > 70:
    #Keep Driving
    print("There's enough fuel")
    fuel -= 1

#For Loop
    movies = ['Star Wars', 'Rocky', 'A-Team']
    for movie in movies:
        print(f"Movie: {movie}")
    
    for i in range(5):
        print(f'i: {i}')

#For Loop - Break and Continue Examples

#Example of using 'Break'
    for count in range(13):
        print(f"{count} times 11 is {count * 11}")
        if count == 7:
            break

#Example of using 'Continue'
    for count in range(13):
        if count == 6:
            continue #Skips 6 x 11 but continues w the rest of the multiplications
        print(f"{count} times 11 is {count *11}")







