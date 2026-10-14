n = int(input("Enter a number: "))
if n < 0:
    print("Factorial of a negative number is not defined.")
elif n == 0:
    print("0! = 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(str(n)+"! = "+str(factorial))