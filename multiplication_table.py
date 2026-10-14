multiplication_table = int(input("Enter the number of which you want the multiplication table: "))
for i in range(1,11):
    if multiplication_table > 0:
        j = multiplication_table * i
        print(str(multiplication_table) + " x " + str(i) + " = " + str(j))
    else:
        print("Please enter a positive number.")