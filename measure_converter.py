# Task-1:
# Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number),    
# converts the entered temperature into Fahrenheit degree and prints the result.

# Task-2:
# Write a short Python program that asks the user to enter a distance (it can be a decimal number) in 
# kilometers, converts the entered distance into miles and prints the result.

temp_Celcius = float(input("Enter the temperature at Celsius degree: "))
temp_Fahrenheit = 1.8 * temp_Celcius + 32
print("Temperature is", temp_Fahrenheit, "\bF", "degree.")


distance1 = float(input("Enter the distance in kilometers: "))
distance2 = distance1 / 1.609344
print(distance2, "mile")