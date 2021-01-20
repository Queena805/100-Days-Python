#choosing a random number between 1 and 100
#make function to set difficulty
# Let the user to guess a number 




from art import logo
import random

#function to check user's guess against actual number
def play_game(level,computer_guess):

  game_continue = True

  if level == 'easy':
    number_of_attempts = 10
  elif level == 'hard':
    number_of_attempts = 5

  while game_continue:
    print(f"You have {number_of_attempts} attempts to guess the number.")

    player_guess = int(input("Please make a guess: "))
    if player_guess > computer_guess:
      print("Too high.")
      number_of_attempts -= 1
    elif player_guess < computer_guess:
      print("Too low.")
      number_of_attempts -= 1
    else:
      game_continue = False
      print(f"You got it! The answer was {computer_guess}.")
    if number_of_attempts <= 0:
      game_continue = False
      print(f"You have {number_of_attempts} attempts left, you lose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


computer_guess = random.randint(1,100)
print(f"Psst, the correct answer is {computer_guess}.")
game_level = input("Choose a difficulty. Type 'easy'or 'hard': ").lower()

play_game(game_level,computer_guess)
