print ("Hello World")
print ("Wow that was really cool")
print("\nQuestion1\n")
print("I love to code in Python.")

print("\nQuestion2\n")

num1 = 2
hado = 4
print(f"I have {num1} cats and {hado} dogs.")

print("\nQuestion3\n")

user_input = input("What's your favourite Ice Cream Flavour?")
user_scoop = int(input("How many scoops of Ice Cream would you like?"))
print(f"Are you sure with {user_input} as your flavour and {user_scoop} for the amount of scoops?")

print(f"OOPS I accidentally dropped half so here you go {user_scoop // 2} breh")

print("\nQuestion4\n")

age = int(input("How old are you?"))

if age > 16:
  print("You are old enough to watch the movie, Have fun!")
elif age == 16:
  print("You are almost old enough..but uh... yeah not quite sorry")
elif age < 16:
  print("You are too young to watch the movie kid, sorry you can come back when you're older, the Movie would probably dead by then tho.")
else:
  print("That is not your age bruh :/")

print("\nQuestion5\n")

Kido = input("")

while True:
  print("Somebody call batman!")
  print("Are you him?")
  Kido = input("Please tell me your name!")
  if Kido == "Batman":
    print("YAY!")
    break
  print("You're not Batman!")

print("\nQuestion 6\n")

secret_number = 6
guesses = 3



#while guesses > 0:
  #guessing = int(input("Can you guess the number between 1-10?"))
  #print(f"You now have {guesses - 1}")

print("\nQuestion 7\n")
#Copy this code into your file.
#Modify the code so that it chooses from 5 possible answers.

import random
 
answer1 = ("Absolutely")
answer2 = ("No way!")
answer3 = ("Go for it.")
answer4 = ("Bruh you're too good!")
answer5 = ("That's Awesome!")
 
print("Welcome to the Magic 8 Ball game. Use it to answer your questions...\n")
 
question = input("Type in your question.\n")
 
print("Shaking....\n" * 4)
 
choice = random.randint(1,3)
 
if choice == 1:
 answer = answer1
elif choice == 2:
 answer = answer2
elif choice == 3:
 answer = answer3
elif choice == 4:
 answer = answer4
elif choice == 5:
  answer = answer5
else:
 answer = answer3
 
print(answer)