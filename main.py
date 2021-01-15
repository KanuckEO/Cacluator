#KanuckEO

op = input("enter a operant(*, /, +, -)")
num1 = input("enter first factor")
num2 = input("enter second number")

if op == '*':
  sum = float(num1) * float(num2)
  print("Here is the answer", sum)

if op == '/':
  sum = float(num1) / float(num2)
  print("Here is the answer", sum)

if op == '+':
  sum = float(num1) + float(num2)
  print("Here is the answer", sum)

if op == '-':
  sum = float(num1) - float(num2)
  print("Here is the answer", sum)