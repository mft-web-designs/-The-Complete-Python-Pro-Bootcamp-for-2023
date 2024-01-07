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

#Write your code below this line 👇

hand_signals = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3:
  print("You typed an invalid number, you lose!")
else:
  print("You chose:")
  print(hand_signals[player_choice])
  
  import random
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(hand_signals[computer_choice])
  
  if player_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
  elif computer_choice > player_choice:
    print("You lose!")
  elif player_choice > computer_choice:
    print("You win!")
  elif computer_choice == player_choice:
    print("It's a draw!")
  
