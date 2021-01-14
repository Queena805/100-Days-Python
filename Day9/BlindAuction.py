from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)




new_dictionary = {}
another_player = 'yes'
while another_player=='yes':

  name = input("What's your name?\n")
  bid_price = int(input("What is your bid?$\n"))
  new_dictionary[name] = bid_price
  another_player= input("Are there any bidders? Type 'yes' or 'no'.\n").lower()
  clear()

highest_bid_price = 0
highest_bidder = ""
for key in new_dictionary:
  price = new_dictionary[key]
  if price > highest_bid_price:
    highest_bid_price = price
    highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid_price}")

