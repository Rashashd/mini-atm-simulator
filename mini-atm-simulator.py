balance = 563
deposit = 0
withdraw = 0

print("Welcome to the ATM!\n\nYour balance is: ", balance, "\n")
print("Please choose an option:\n\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n")

choice = int(input("Enter your choice: "))

while choice != 4:
   
    if choice == 1:
        print("Your current balance is: ", balance, "\n")
    
    elif choice == 2:
        deposit = int(input("Enter amount to deposit: "))
        if deposit > 0:
            balance = balance + deposit
            print("Deposit successful! New balance: ", balance, "\n")
        else:
            print("Please try again!")
    
    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance = balance - withdraw
            print("Withdraw successful! New balance: ", balance, "\n")
        else:
            print("Insufficient Funds!\n")
    
    else:
        print("Invalid option!\n")
    
    print("Please choose an option:\n\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n")
    choice = int(input("Enter your choice: "))

print("Thank you for choosing this ATM\nGoodbye!")
