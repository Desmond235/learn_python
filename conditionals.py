operator = input("Enter an operator (+ - * /)")
if operator not in ['+', '-', '*', '/']:
    print(f"{operator} is not a valid operator")
    exit(0)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = 0

def print_result(res):
    print(round(res, 3))

if operator == '+':
    result = num1 + num2
    print_result(result)
elif operator == "-":
    result = num1 - num2
    print_result(result)
elif operator =="*":
    result= num1 * num2
    print_result(result)
elif operator == "/":
    result = num1 / num2
    
print_result(result)