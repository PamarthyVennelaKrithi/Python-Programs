Number = float(input("Enter a number: "))
if Number % 2 == 0:
    print("The given number is even.")
elif Number % 2 == 1:
    print("The given number is odd.")
else:
    print("The given number is a decimal. It is neither even nor odd.")