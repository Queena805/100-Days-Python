#import art
import random
from art import logo, vs
from game_data import data
from replit import clear


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """format the acct dat into printable formats."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return (f"{account_name},a {account_descr}, from {account_country}")


def check_answer(player_guess, a_followers, b_followers):
    """Take the user guess and follower acounts and returns if they got it right."""
    if a_followers > b_followers:
        return player_guess == 'a'
    else:
        return player_guess == 'b'


def game():
    print(logo)
    score = 0
    game_should_continue = True
    compare_a = get_random_account()
    compare_b = get_random_account()
    #Make the game repeatable.
    while game_should_continue:
        #generate a random acct from the game data.
        #Making account at position B become the next position A

        compare_a = compare_b
        compare_b = get_random_account()
        while compare_a == compare_b:
            compare_b = get_random_account()

        print(f"Compare A: {format_data(compare_a)}.")
        print(vs)
        print(f"Against B: {format_data(compare_b)}.")

        #Ask user for a guess

        player_guess = input(
            "Who have more followers? Type 'A' or 'B': ").lower()

        #Check if the user is correct
        a_follower_account = compare_a['follower_count']
        b_follower_account = compare_b['follower_count']

        is_correct = check_answer(player_guess, a_follower_account,
                                  b_follower_account)

        #Clear the screen betwee rounds.
        clear()
        print(logo)
        #Give user feedback on their guess
        ##Score keeping.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Oops, that's wrong. Finallt score: {score}.")


game()

