#Number Guessing Game Objectives:
#from art import logo
import random
difficulty = ""
# Include an ASCII art logo.
#print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5
number = random.randint(1,100)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
for _ in range(attempts):
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
# If they got the answer correct, show the actual answer to the player.
  if guess == number:
    print(f"You got it! The answer was {number}.")
    break
  elif guess > number:
    print("Too high.")
  else:
    print("Too low.")
# Track the number of turns remaining.
  attempts -= 1
  # If they run out of turns, provide feedback to the player. 
  if attempts == 0:
    print("You've run out of guesses, you lose.")
