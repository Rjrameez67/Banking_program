def show_balance():
    print(f"You current balance is ${balance}")

def deposit():
        amount = int(input("Enter the amount you want to deposit:"))
        if amount < 0:
            print("your withdrawal amount is below 0")
            return 0
        else:
            return amount
balance = 0
is_running = True

def withdraw():
    amount_withdrawal = int(input("How much money you want to withdraw?:"))
    if amount_withdrawal > balance:
        print("Insufficient balance!!!")
        return 0
    elif amount_withdrawal < 0:
        print("Your Minimum Amount has to be above 0")
        return 0
    else:
        return amount_withdrawal
while is_running:
    print("-----------------------")
    print("---Welcome to Bank------")
    print("-----------------------")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = input("What service You want sir/Mam?(1-4):")



    if choice == "1":
            show_balance()
    elif choice == "2":
            balance += deposit()
    elif choice == "3":
            balance -= withdraw()
    elif choice == "4":
            is_running = False
    else:
            print("Invalid Input")
print("-----------------------")
print("Thank you for Visiting the bank!!!")
print("-----------------------")