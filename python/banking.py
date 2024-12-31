class BankAccount:
  def __init__(self, account_number, account_name, balance=0):
    self.account_number = account_number
    self.account_name = account_name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited ${amount}. Current balance: ${self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds.")
    else:
      self.balance -= amount
      print(f"Withdrew ${amount}. Current balance: ${self.balance}")

def main():
  account = BankAccount("123456789", "John Doe", 1000)
  while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
      amount = float(input("Enter amount to deposit: "))
      account.deposit(amount)
    elif choice == 2:
      amount = float(input("Enter amount to withdraw: "))
      account.withdraw(amount)
    elif choice == 3:
      print(f"Current balance: ${account.balance}")
    elif choice == 4:
     break
    else:
     print("Invalid choice")

if __name__ == "__main__":
  main()

