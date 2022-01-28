########## Number Guessing Game ##########

# 1. Imports
from art import logo
import random

# 2. Print logo and Welcome
print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

# 3. Generate a random number between 1 and 100
answer = random.randint(1, 100)
# --->>> Testing
print(f"Pssst, the correct answer is {answer}")


# 4. Define a functions for operations

def user_choice():
    easy_hard = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    if easy_hard == "easy":
        return 11
    elif easy_hard == "hard":
        return 5

def guess():
    turns = user_choice()
    if turns != 0:
        while turns != 0:
            print(f"\nYou have {turns} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print(f"Invalid guess!\nIt should be between 1 and 100.")
                turns -= 1
            elif guess == answer:
                print(f"You got it! The answer was {answer}!\n\n")
                turns = 0
            elif guess > answer:
                print(f"Too HIGH!\n")
                turns -= 1
                if turns != 0:
                    print("Guess again...")
            elif guess < answer:
                print(f"Too LOW!\n")
                turns -= 1
                if turns != 0:
                    print("Guess again...")
    elif turns == 0:
        print(f"You've run out of guesses, you lose.\n\n")

        
            

guess()








# for turn in range(turns):
    
    
    


