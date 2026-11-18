
import csv
import matplotlib.pyplot as plt

# Create sales data
sales = [
    ["Product", "Sales"],
    ["Laptop", 50000],
    ["Mobile", 30000],
    ["Tablet", 20000],
    ["Headphones", 10000],
    ["Keyboard", 5000]
]

# Store data in CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales)

# Read CSV file
products = []
amounts = []

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        products.append(row[0])
        amounts.append(int(row[1]))

# Display sales details
print("----- Retail Sales Report -----")

for i in range(len(products)):
    print(products[i], ":", amounts[i])

print("Total Sales:", sum(amounts))

# Create bar chart
plt.bar(products, amounts)
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
