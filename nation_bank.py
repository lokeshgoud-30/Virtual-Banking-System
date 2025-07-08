from abc import ABC, abstractmethod
import random
from datetime import datetime
# Abstract Class
class Account(ABC):
    @abstractmethod
    def deposit(self, amount): pass
    @abstractmethod
    def withdraw(self, amount): pass
    @abstractmethod
    def ministatement(self): pass
# Main Bank Class
class Bank(Account):
    bankname = "Nation Bank"
    branch = "Cloud Branch"
    def __init__(self, username, mobile, address, pin):
        self.username = username
        self.mobile = mobile
        self.address = address
        self.__pin = pin
        self.__balance = 0.0
        self.account_number = "NBC" + str(random.randint(10000000, 99999999))
        self.ifsc_code = "NBIN0NAT123"
        self.history = []
        print("\nFor account creation, we need your basic details.")
        print("Your account has been created successfully.")
        print(f"Account Number: {self.account_number}")
        print(f"Branch: {self.branch}")
        print(f"IFSC Code: {self.ifsc_code}")
    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.__pin
    def deposit(self, amount):
        if self.verify_pin():
            self.__balance += amount
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.history.append(f"[{now}] Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Incorrect PIN. Transaction denied.")
    def withdraw(self, amount):
        if self.verify_pin():
            if amount <= self.__balance:
                self.__balance -= amount
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.history.append(f"[{now}] Withdrawn ${amount}")
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect PIN. Transaction denied.")
    def ministatement(self):
        if self.verify_pin():
            print(f"Your current balance is ${self.__balance}")
        else:
            print("Incorrect PIN. Access denied.")
    def show_history(self):
        if self.verify_pin():
            print("\nTransaction History:")
            if not self.history:
                print("No transactions yet.")
            for entry in self.history:
                print(entry)
        else:
            print("Incorrect PIN. Access denied.")
# Inherited Account Types
class SavingsAccount(Bank):
    def account_type(self):
        print("You are using a Savings Account")
class PremiumAccount(Bank):
    def account_type(self):
        print("You are using a Premium Account with extra benefits")
# ---------------- Main Program ----------------
print(f"\nWelcome to {Bank.bankname} - {Bank.branch}")
username = input("Enter your name: ")
mobile = input("Enter your mobile number: ")
address = input("Enter your address: ")
pin = input("Set PIN: ")
# Choose account type
print("\nChoose account type:")
print("1. Savings\n2. Premium")
acc_choice = input("Enter choice: ")
if acc_choice == "1":
    user_acc = SavingsAccount(username, mobile, address, pin)
elif acc_choice == "2":
    user_acc = PremiumAccount(username, mobile, address, pin)
else:
    print("Invalid option. Defaulting to Savings.")
    user_acc = SavingsAccount(username, mobile, address, pin)
user_acc.account_type()
# Banking menu loop
while True:
    print("\nChoose an option:")
    print("1. Deposit\n2. Withdraw\n3. Mini Statement\n4. Transaction History\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: $"))
        user_acc.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: $"))
        user_acc.withdraw(amount)
    elif choice == "3":
        user_acc.ministatement()
    elif choice == "4":
        user_acc.show_history()
    elif choice == "5":
        print("\nLogged out. Thanks for choosing Nation Bank!")
        break
    else:
        print("Invalid option. Please try again.")
