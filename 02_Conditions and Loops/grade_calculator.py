marks = float(input("Enter your marks: "))
if marks >= 0 and marks <= 100:
    if marks > 95:
        print("You got an O+ grade.")
    elif marks > 90:
        print("You got an O grade.")
    elif marks > 85:
        print("You got an A+ grade.")
    elif marks > 80:
        print("You got an A grade.")
    elif marks > 75:
        print("You got a B+ grade.")
    elif marks > 70:
        print("You got a B grade.")
    elif marks > 65:
        print("You got a C grade.")
    elif marks > 60:
        print("You got a D grade.")
    elif marks >= 35:
        print("You got a P grade.")
    else:
        print("You got a F grade.")
else:
    print("Invalid marks. Please enter the marks between 0 and 100.")