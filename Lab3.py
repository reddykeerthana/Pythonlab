
import csv

filename = "payroll.csv"

while True:
    print("\n1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter basic salary: "))

        hra = salary * 0.20
        da = salary * 0.10
        total = salary + hra + da

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow(["Name", "ID", "Basic Salary",
                                 "HRA", "DA", "Total Salary"])

            writer.writerow([name, emp_id, salary,
                             hra, da, total])

        print("Payroll saved successfully!")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                print("\nPayroll Details:")
                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("Payroll file not found!")

    elif choice == "3":
        print("Exiting Payroll System!")
        break

    else:
        print("Invalid choice!")
