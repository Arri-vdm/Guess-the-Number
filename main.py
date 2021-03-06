########## Number Guessing Game ##########

# 1. Imports
from art import logo
from random import randint

# 2. Print logo and Welcome
print(logo)
print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")

# 3. Generate a random number between 1 and 100
answer = randint(1, 100)

# --->>> Testing:
# print(f"Pssst, the correct answer is {answer}")

# Global Variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# 4. Define functions for operations
# 4.1 Function 1
def user_choice():
    """TAKES an input from the user:\n
    --->> Choose a difficulty. Type 'easy' or 'hard'\n
    - If 'easy' is chosen, user gets 10 turns.\n
    - If 'hard' is chosen, user gets 5 turns.\n
    --->> RETURNS: the number of turns\n
    """
    easy_hard = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    if easy_hard == "easy":
        return EASY_LEVEL_TURNS
    elif easy_hard == "hard":
        return HARD_LEVEL_TURNS


# 4.2 Function 2
def guess():
    """The GAME's MAIN FUNCTION:\n
        Performs all the operations of the game.\n
        --->> Takes in the user_choice() function:\n
        - It contains the number of turns\n
        --->> It contains a nested function guess_again():\n
        - Checks whether turns are equal or not equal to zero\n
        --->> RETURNS: The game itself\n
    """
    # Calls the user_choice function and assigns its return
    # to turns
    turns = user_choice()

    # 4.3 Function 3 = Nested
    def guess_again(turns_left):
        """A NESTED FUNCTION):\n
            --->> Checks whether turns are equal or
                not equal to zero\n
            - If zero turns prints out a message in correct          place\n
            - If not zero turns prints out a message in correct      place\n          
        """
        if turns != 0:
            print("Guess again...")
        elif turns == 0:
            print(
                f"\nYou've run out of guesses, you lose.\nThe number was {answer}!\n\n"
            )

    while turns != 0:
        # Prints remaining turns
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        # Get the guess from the user
        guess = int(float(input("Make a guess: ")))
        # Series of if, elif statements to
        # compare the guess with the answer
        if guess < 1 or guess > 100:
            print(f"Invalid guess!\nIt should be between 1 and 100.")
            turns -= 1
        elif guess == answer:
            print(f"\nYou got it! The answer was {answer}!\n\n")
            turns = 0
        elif guess > answer:
            print(f"Too HIGH!")
            turns -= 1
            # Calls the guess again function
            guess_again(turns_left=turns)
        elif guess < answer:
            print(f"Too LOW!")
            turns -= 1
            # Calls the guess again function
            guess_again(turns_left=turns)


# Call the MAIN function
guess()
