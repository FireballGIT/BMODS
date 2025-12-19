def load(ext):
  #do this later, but it's supposed to load extensions for stuff like triginometry, calculus, and more.

def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def product(num1, num2):
  return num1 * num2

def div(dividend, divisor):
  return dividend / divisor

def exp(i, n):
  return i ** n

def floor(num1, num2):
  return num1 // num2

def calculator():
  print("CalcuFunction Calculator")
  op = int(input("ENTER OPERATOR(+, -, *, /, //, or ^): "))
  n1 = int(input("ENTER 1st NUMBER: "))
  n2 = int(input("ENTER 2nd NUMBER: "))
  if op == "+":
    print(add(num1, num2))
  elif op == "-":
    print(sub())
  elif op == "*":
    print(product(n1, n2))
  elif op == "/":
    print(div(n1, n2))
  elif op == "//":
    print(floor(n1, n2))
  elif op == "^":
    print(exp(n1, n2))
  else:
    print("ERROR! Invalid operator!")
