temp1 = input("Convert from: ")
temp2 = input("Convert into: ")
if temp1 == "C" and temp2 == "F":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("F = " + str(fahrenheit) + "°F")
elif temp1 == "F" and temp2 == "C":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("C = " + str(celsius) + "°C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")