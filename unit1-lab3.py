# Restaurant Bill Calculator

print("========== RESTAURANT BILL ==========")

food = float(input("Enter food bill: "))
drinks = float(input("Enter drinks bill: "))
dessert = float(input("Enter dessert bill: "))

subtotal = food + drinks + dessert
tax = subtotal * 0.05
total = subtotal + tax

print("\n----------- BILL -----------")
print("Food     :", food)
print("Drinks   :", drinks)
print("Dessert  :", dessert)
print("Subtotal :", subtotal)
print("Tax 5%   :", tax)
print("Total    :", total)
print("----------------------------")
print("Thank you for visiting!")