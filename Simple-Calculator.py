
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: \n"))

for symbol in operations:
  print(symbol)
operation_symbol = input("\nPick an operation from the line above: \n")

num2 = int(input("What's the second number?: \n"))
calculation_function = operations[operation_symbol]

print(f"{num1} {operation_symbol} {num2} = {calculation_function(num1, num2)}")
