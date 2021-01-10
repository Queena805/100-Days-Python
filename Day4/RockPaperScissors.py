
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
game_list = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_list[player_choose])

print("Computor chose:")

computer_choose = random.randint(0,2)
print(game_list[computer_choose])

if game_list[computer_choose]== game_list[player_choose] :
  print("It\'s a draw.")
elif  game_list[computer_choose]== game_list[player_choose-1]:
  print("You win!")
else:
  print("You lose.")


  




