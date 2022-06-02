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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

users_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
if users_choice >= 3 or users_choice < 0:
  print("You have typed an invalid number. You lose!")
else:
  print(game_images[users_choice])
  
  computer_choice = random.randint(0,2)
  print(f"The computer picks: ")
  print(game_images[computer_choice])
  
  if users_choice == 0 and computer_choice == 1:
    print("You win")
  elif users_choice == 1 and computer_choice == 0:
    print("You lose")
  elif users_choice == 2 and computer_choice == 0:
    print("You lose")
  elif users_choice == 0 and computer_choice == 2:
    print("You win")
  elif users_choice == 1 and computer_choice == 2:
    print("You lose")
  elif users_choice == 2 and computer_choice == 1:
    print("You win")
  elif users_choice == computer_choice:
    print("It is a draw!")



