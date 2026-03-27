import csv

# Add expense
def add():
    date = input("Enter date: ")
    amount = input("Enter amount: ")

    file = open("expenses.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow([date, amount])
    file.close()

    print("Expense added!")

# View expenses
def view():
    file = open("expenses.csv", "r")
    reader = csv.reader(file)

    for row in reader:
        print(row)

    file.close()

# Menu
while True:
    print("\n1.Add  2.View  3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        break
    else:
        print("Wrong choice")