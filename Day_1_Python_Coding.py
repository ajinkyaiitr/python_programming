# Write your code below this line 👇
print("Hello World!!\nHello World!!\nHello World!!")
###The double quotes indicate the beginning and end of the string characters
##/n is the syntax for newline
##Concatenation

print("Hello" + " " + "Angela")
print("Hello" + " " + "Angela")

##Code Challenge

print("Day 1 - String Manipulation")
print("String Concatenation is done with the" + " +" + "sign.")
print('e.g. print("Hello" + "world")')
print("New lines can be created with a blackslash and n.")

#Input Function

input("What is your Name Gentleman?")

#Write a program that prints the number of characters in a user's name.
print("Hello " + input("What is your name?") + "!")
print(len(input))

Write a program to find the length of your name
#print("Hello " + input("What is your name?") + "!")
name = input("What is your name? ")
print("The length of your name is:", +len(name))



#Write a program that switches the values stored in the variables a and b

a = input("a:")
b = input("b:")

c = a
a = b
b = c
print("The value of a is:" + a)
print("The value of b is:"+ b)



#Write a program to generate BAND Name



print("Welcome to Band-Name Generator!!")

city = input("What's the name of the city you grew up in ?")
pet = input("What's your pet name ?")
print("Your Band Name can be " +city + " " +pet)


=======================================================
Day 2
Understanding Data-Types and how to manipulate strings
-----------------------------------------------------

Primitive Data Types

Strings | Integers | Float | Boolean

The method of pulling a particular Element from String is called Subscript

Type Casting - When we change the datatype from one type to another


print(3+5)
print(7-4)
print(3 * 2)
print(3 ** 2)
PEMDAS rule
P-Paranthesis
E - Exponential
M - Multiplication
D - Division
A - Addition
S - Subtraction


##BMI Calculator Exercise

Write a program to calculate BMI from weight and height

height = input("Enter your height in meters:")
weight = input("Enter your weight in kg:")
weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
print(bmi)


OUTPUT:

Enter your height in meters:1.8
Enter your weight in kg:64
19.753086419753085
 


@Create a program using maths and f-strings that tells us how many days,weeks, months we have left if we live until 90 years olf
It will take your current age as input and output a message with our time left in this format


age = input("What is your current age?")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(days_remaining)
print(weeks_remaining)
print(months_remaining)
message = f"You have {days_remaining} days , {weeks_remaining} weeks , {months_remaining} months"
print(message)

#Write a program to calculate the tip of a hotel

print("Welcome to the tip calculator")
total_bill = input("What was the total bill?")
t_bill = float(total_bill)
tip_percentage = input("What percentage tip would you like to give?")
tip_p = int(tip_percentage)
final_tip = tip_p/100 * t_bill
t_bill = t_bill + final_tip
no_of_person = input("How many people to split the bill?")
p_person = int(no_of_person)
per_pay = t_bill/p_person
message = f"Per person have to pay $ {per_pay}"
print(message)

OUTPUT:

Welcome to the tip calculator
What was the total bill?600
What percentage tip would you like to give?10
How many people to split the bill?6
Per person have to pay $ 110.0
 



