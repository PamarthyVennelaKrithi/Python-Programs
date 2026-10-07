num1 = float(input("First number: "))
operater = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))
if operater == "+":
    print(num1 + num2)
elif operater == "-":
    print(num1 - num2)
elif operater == "*":
    print(num1 * num2)
elif (operater == "/" and num2 != 0):
    print(num1 / num2)
else:
    print("Invalid operator or division by zero is undefined.")