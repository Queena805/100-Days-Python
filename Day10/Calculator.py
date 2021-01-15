#calculator
from replit import clear
from art import logo

#add
def add(n1,n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def devide(n1, n2):
  return n1/n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = devide

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))

  for symbol in operations:
    print(symbol)
    
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)

    print(f"{num1}{operation_symbol}{num2} = {answer}")

    result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if result == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()





 
