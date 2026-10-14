n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if (n % i) == 0 and n != i:
            print(str(n) + " is a composite number")
            break
    else:
        print(str(n) + " is a prime number")
else:
    print(str(n) + " is neither prime nor composite number")