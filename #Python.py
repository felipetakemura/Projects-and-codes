#Python.tutorials
print("Hello World")
#Variables=value (string,integer,float,boolean)
#Strings
first_name = "Felipe"
print(f"Hello {first_name}")
#Integers 
age = 14
print(f"You are {age} years old")
#Float 
price = 15.99
print(f"The price is ${price}")
#Boolean
is_student = True
print("You are a student")

#Typecasting
first_name = "Felipe"
age = 14
price = 15.99
is_student = True
print(type(is_student))

#Input
name =input("What's your name?: ")
print(f"Hello {name}")
age = int(input("How old are you?: "))
age = age + 1
print("Happy Birthday")
print(f"You are {age} years old")
#Exercise 1
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width 
print(f"The area is {area}cm")
#Exercise 2 
item = input("What's the item?: ")
price = float(input(f"What's the price of {item}: "))
quantity = int(input(f"What's the quantity of {item}:"))
total = price * quantity 
print(f"The total of {item} is ${total}")

#Madlibs game
adjective1 = input("Enter an adjective (depscription): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (depscription): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (depscription): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

#math exercises
import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi *radius

print(f"The circumference is: {round(circumference, 2)}")

import math

radius = float(input('Enter the radius of a circle: '))
area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(area, 2)}cm^2")

import math
a = float(input("Enter side of A: "))
b = float(input("Enter side of B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The C side is: {round(c, 2)}cm^2")

#if exercises
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old for this!")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You need to be 18+ to sign up!")

response = input("Do you want food? (Y/N): ")

if response == ("Y"):
    print("Go have some food!")
else:
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You didn't type your name!")
else:
    print(f"Hello {name}")

for_sale = False
if for_sale:
    print("This item is for sale")
else:
    print("This item is not available")

online = True
if online:
    print("The user is online")
else:
    print("The user if offline")

#Python calculator 

operator = input("Enter the operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

#Weight conversion program
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit= "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

#Temperature conversion program
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")

#Logical operators
temp = 35
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

temp = 14
is_sunny = False
if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("IT is cloudy")
elif temp < 0 and not is_sunny:
    print("It is COLD outside")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is cloudy") 

#Conditional expression 
num = -5
print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

user_role ="admin"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(f"Your access level is {access_level}")

#String methods

name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")
result = name.rfind("e")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
phone_number = phone_number.replace("-", "")
print(phone_number)

#print(help(str))

#Validate username
username = input("Enter your username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't countain spaces")
elif not username.isalpha():
    print("Your username can't countain numbers")
else: 
    print(f"Welcome {username}")

#Indexing

credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::2])
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#Format specifiers
price1 = 3.14159
price2 = -974.65
price3 = 122200965578

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

#While loops name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Entet your age: "))

while age < 0: 
    print("This age is not valid")
    age = int(input("Entet your age: "))

print(f"You are {age} years old!")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")

#Python compound interest calculator
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else: 
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years/s: ${total:2f}")