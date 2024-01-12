#Number Guessing Game Objectives:
from art import logo
import random

#Set up some GLOBAL variables
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

#define functions check_answer
def check_answer(guess, answer, attempts):
  """checks answer against guess. Returns the updated number of attempts remaining."""
  if guess > answer:
    print("Too high.")
    return attempts - 1
  elif guess < answer:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {answer}.")

 #define function set_difficulty
def set_difficulty():
  """Gets the difficulty from the user and sets up the maximum number of attempts they can make."""
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_ATTEMPTS
  else:
    return HARD_LEVEL_ATTEMPTS

#define the main game as a function
def game():
  print(logo)
  # Allow the player to submit a guess for a number between 1 and 100.
  print("Welcome to the Number guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.randint(1,100)
  #DEBUG: display the target number if needed for checking purposes
  #DEBUG: print(f"Pssst, the correct answer is {number}") 
  
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  attempts = set_difficulty()
  #DEBUG: print(f"We have {attempts} attempts to guess this number...")
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
  # If they got the answer correct, show the actual answer to the player.
    attempts = check_answer(guess, number, attempts)
    if attempts == 0:
      print(f"You've run out of guesses, you lose. The correct number was: {number}")
      return
    elif guess != number:
      print("Guess again.")

game()
