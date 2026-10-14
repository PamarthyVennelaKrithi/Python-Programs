num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(str(num1) + " is the largest number.")
elif num2 > num1 and num2 > num3:
    print(str(num2) + " is the largest number.")
elif num3 > num1 and num3 > num2:
    print(str(num3) + " is the largest number.")
elif num1 == num2 and num1 > num3:
    print(str(num1) + " is the largest numbers.")
elif num1 == num3 and num1 > num2:
    print(str(num1) + " is the largest numbers.")
elif num2 == num3 and num2 > num1:
    print(str(num2) + " is the largest numbers.")
else:
    print("All three numbers are equal.")