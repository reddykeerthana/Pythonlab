# Mini Project: Multi-Unit Converter

print("================================")
print("       SMART UNIT CONVERTER")
print("================================")

print("1. Kilometers -> Miles")
print("2. Kilograms -> Pounds")
print("3. Liters -> Milliliters")
print("4. Hours -> Minutes")
print("5. Celsius -> Fahrenheit")

choice = int(input("\nSelect an option: "))

if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print("Distance in miles:", round(miles, 2))

elif choice == 2:
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print("Weight in pounds:", round(pounds, 2))

elif choice == 3:
    liters = float(input("Enter volume in liters: "))
    ml = liters * 1000
    print("Volume in milliliters:", ml)

elif choice == 4:
    hours = float(input("Enter time in hours: "))
    minutes = hours * 60
    print("Time in minutes:", minutes)

elif choice == 5:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2))

else:
    print("Invalid option!")

print("\nConversion completed successfully!")
