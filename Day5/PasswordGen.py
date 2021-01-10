#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# random_letter = []
# for letter in range(0, nr_letters):
#   random_pick = random.randint(0, len(letters)-1)
#   random_letter.append(letters[random_pick])
# random_symbol = []
# for letter in range(0, nr_symbols):
#   random_pick = random.randint(0, len(symbols)-1)
#   random_symbol.append(symbols[random_pick])
# random_number = []
# for letter in range(0, nr_numbers):
#   random_pick = random.randint(0, len(numbers)-1)
#   random_number.append(numbers[random_pick])

# password_list = ''.join(random_letter + random_symbol + random_number)
# print(f"Your password is: {''.join(random.sample(password_list,len(password_list)))} ")

password_list = []
for char in range (1, nr_letters + 1):
  password_list += random.choice(letters)
for char in range(1 , nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers +1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char
print(f"You password is: {''.join(password_list)}")



