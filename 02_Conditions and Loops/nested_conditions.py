user_name = input("Username: ")
password = input("Password: ")
if user_name == "Vennela":
    if password == "Vennela@2003":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")