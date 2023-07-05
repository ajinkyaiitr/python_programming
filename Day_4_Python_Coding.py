****Randomization and Python Lists****

1.The mersenne twister is a pseudo-random number generator.It is by far mostly used PRNG and Python uses it extensive

# import random

# print("Welcome to virtual coin-toss program")
# random_int = random.randint(0,1)
# if random_int == 1:
#   print("Heads")
# else:
#   print("Tails")
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-1])


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

@@Banker Roulette Program

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
num_items = len(names)
#Get the total no of items in the list
print(num_items)
#Generate random numbers between 0 and last item in the list
random_choice = random.randint(0, num_items - 1)
#print(random_choice)
#Pick out the name from the list of names using random choice number
who_will_pay = names[random_choice]
#Write your code below this line 👇
print(who_will_pay + "is going to buy the meal today!")

# # Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
# num_items = len(names)
# print(num_items)

#Index of out range Program

# Nested 8Lists

# fruits = ["Apple","Orange","Banana","Pineapple","Strawberry"]
# vegetables = ["Brinjal","Tomato","Onion","Pumpkin","Bittergourd"]
# dirty_dozens = [fruits,vegetables]
# print(dirty_dozens)
#=========================
##Treasure Map Program

# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜","⬜"]
# map_row = [row1, row2, row3]
# print(f"{row1}\n{row2} \n{row3}")
# position = input("Where do you want to put the treasure?")
# horizontal = int(position[0])
# print(horizontal)
# vertical = int(position[1])
# print(vertical)
# map_row[vertical - 1] [horizontal - 1] = "X"
# print(f"{row1}\n{row2} \n{row3}")

###Write a program to prepare Rock , Papers , Scissors Game 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
  
  
  ====================================================
