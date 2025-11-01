# Robert Potter, 11/10/2025, Milestone 2

#Import random module
import random

#store Random Number
Random_Number = random.randint(1,100)

#Ask User for name and greet them
User_Name = input("Please enter your name: ")
print(f"Hello {User_Name}!, Please Guess a number between 1 and 100.")

#For loop to allow user to guess up to 6 times
for Guess_Attempt in range(1,7):
    User_Guess = int(input(f"Attempt {Guess_Attempt}: Enter your guess: "))
#Check if the guess is too low, too high, or correct    
    if User_Guess < Random_Number:
        print("Your guess is too low.")
    elif User_Guess > Random_Number:
        print("Your guess is too high.")
#If correct, congratulate and break the loop
    else:
        print(f"Congratulations {User_Name}! You've guessed the correct number {Random_Number} in {Guess_Attempt} attempts!")
        break
#If user fails to guess in 6 attempts, reveal the number
else:
    print(f"Sorry {User_Name}, you've used all your attempts. The correct number was {Random_Number}. Better luck next time!")
