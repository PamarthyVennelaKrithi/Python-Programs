Age = int(input("Enter your age: "))
if(Age < 18 and Age >= 0):
    print("You are a minor.")
elif(Age >= 18 and Age < 60):
    print("You are a major.")
elif(60 <= Age):
    print("You are a senior citizen.")
else:
    print("Invalid input. Please enter a valid age.")