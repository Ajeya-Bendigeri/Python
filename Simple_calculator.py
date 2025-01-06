
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("Enter operation (+, -, *, /): ")

if opr == '+':
    result = num1 + num2
elif opr == '-':
    result = num1 - num2
elif opr == '*':
    result = num1 * num2
elif opr == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

print(f"The result is: {result}")
