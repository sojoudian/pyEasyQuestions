balance = 0.0

while True:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Choose an action: ")
    
    try:
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"${amount} deposited.")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"${amount} withdrawn.")
        elif choice == "3":
            print(f"Your balance is ${balance}.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Please enter a valid number.")

