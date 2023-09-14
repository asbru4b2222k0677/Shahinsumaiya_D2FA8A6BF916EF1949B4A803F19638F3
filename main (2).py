class BankAccount:

  def __init__(self, account_number,                account_holder_name,                initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount >0:
      self.__account_balance += amount
      print("Deposited rupees is{}.  New balance:{}".format(amount, self.__account_balance))
    else:
      print("Invalid deposit amount.please deposit a positive amount.")

  def withdraw(self, amount):
    if amount >0 and amount<=   self.__account_balance:
      self.__account_balance -=amount
      print("withdraw rupees is{}.New balance:{}". format (amount, self.__account_balance))

    else:
       
      print("Invalid withdraw amount or insufficient balance.")

  def display_balance(self):
      print("Account balance for {} (Account #{}): rupees {}". format (
        self.__account_holder_name,self.__account_number,
        self.__account_balance))

account= BankAccount(account_number="12345678", account_holder_name="Shahin", initial_balance=6000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
   