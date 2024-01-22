def add(num1, num2):
    result = num1 + num2
    print(f"The result is: {result}")

def subtract(num1, num2):
    result = num1 - num2
    print(f"The result is: {result}")

def multiply(num1, num2):
    result = num1 * num2
    print(f"The result is: {result}")

def divide(num1, num2):
    if num2 != 0.0:
        result = num1 / num2
    else:
        result = 0
    print(f"The result is: {result}")

def mod(num1, num2):
    result = num1 % num2
    print(f"The result is: {result}")
    
def calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    symbol = input("Enter the operator: ")

    if symbol == "+":
        add(num1, num2)
    elif symbol == "-":
        subtract(num1, num2)
    elif symbol == "*" or symbol == "x":
        multiply(num1, num2)
    elif symbol == "/":
        divide(num1, num2)
    elif symbol == "%" or symbol == "mod":
        mod(num1, num2)
    else:
        print("Invalid symbol")

while True:
    calculate()
    do_continue = input("Enter n to stop calculating: ")
    if do_continue == "n":
        break