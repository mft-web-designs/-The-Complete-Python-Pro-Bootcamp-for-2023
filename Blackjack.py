############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from art import logo
from replit import clear


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card  

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"
  
  
def play_game():
  user_cards = []
  computer_cards = []
  print(logo)
  # Let's start.....
  #The user and computer should each get 2 random cards.
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  draw_card = "y"
  while draw_card == "y":
  
    #DEBUG
    print(f"User has been dealt: {user_cards}\nComputer has been dealt: {computer_cards[0]}")
    #Add up the user's and the computer's scores.
    calculate_scored_user = calculate_score(user_cards)
    calculate_scored_computer = calculate_score(computer_cards)
    
    #DEBUG
    #print(f"User score is: {calculate_scored_user}\nComputer score is: {calculate_scored_computer}")
    
    #Does the user or computer have a blackjack? (ace + 10)
    if calculate_scored_user ==21 or calculate_scored_computer == 21:
      print("Blackjack!")
      if calculate_scored_user == 21:
        print("You win!")
        break
      else:
        print("You lose!")
        break
        
    #Is user's score over 21?
    if calculate_scored_user > 21:
      if 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
        calculate_scored_user = calculate_score(user_cards)
        if calculate_scored_user > 21:
          print("You lose!")
          break
      else:
        print("You lose!")
        break
    
    #Ask the user if they want to get another card.
    draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
    if draw_card == "y":
      user_cards.append(deal_card())
      calculate_scored_user = calculate_score(user_cards)
    else:
      draw_card = "n"
      break
    
  while calculate_scored_computer != 0 and calculate_scored_computer < 17:
    computer_cards.append(deal_card())
    calculate_scored_computer = calculate_score(computer_cards)
    
  #Reveal cards
  print(f"    Your final hand: {user_cards}, final score: {calculate_scored_user}")
  print(f"    Computer's final hand: {computer_cards}, final score: {calculate_scored_computer}")
  print(compare(calculate_scored_user, calculate_scored_computer))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
