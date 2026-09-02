# Shopping Bill Calculator

print("========== SHOPPING BILL ==========")

item = input("Enter item name: ")
price = float(input("Enter price of one item: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = subtotal * 0.10
final_amount = subtotal - discount

print("\n----------- BILL -----------")
print("Item       :", item)
print("Price      :", price)
print("Quantity   :", quantity)
print("Subtotal   :", subtotal)
print("Discount   :", discount)
print("Final Bill :", final_amount)
print("----------------------------")