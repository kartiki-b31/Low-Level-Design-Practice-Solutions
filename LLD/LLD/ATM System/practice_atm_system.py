from abc import ABC, abstractmethod
import datetime
import threading

# Creating the Account class
class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    # Creating the get_account_number method
    def get_account_number(self):
        return self.account_number

    # Creating the Check Balance Method
    def get_balance(self):
        return self.balance

    # Creating the verify_pin method
    def verify_pin(self, entered_pin):
        return self.pin == entered_pin
    
    # Creating the Debit Method
    def debit(self, amount):
        self.balance -= amount
    
    # Creating the Credit method
    def credit(self, amount):
        self.balance += amount

# Creating the Card Class
class Card:
    def __init__(self, card_number):
        self.card_number = card_number
    
    # Creating the get_card_number method
    def get_card_number(self,):
        return self.card_number
    
# Crreating the Abstract Transaction Class
class Transaction(ABC):
    def __init__(self, transaction_id, account, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
    
    # Creating an abstract method execute
    def execute(self):
        pass

# Creating the Withdrawal Treansaction Class
class WithdrawalTransaction(Transaction):
    def __init__(self, transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)
    
    # Creating the exeute method
    def execute(self):
        self.account.debit(self.amount)
    
# Creating the Withdrawal Treansaction Class
class DepositeTransaction(Transaction):
    def __init__(self, transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)
    
    # Creating the exeute method
    def execute(self):
        self.account.credit(self.amount)
    
# Creating the Banking Service Class
class BankingService:
    def __init__(self):
        self.accounts = {}
    
    # Creating the create_account method
    def create_account(self, account_number, initial_amount, pin):
        self.accounts[account_number] = Account(account_number, initial_amount, pin)

    # Creating the get_account method
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    # Creating the method for process_transaction
    def process_transaction(self, transaction):
        transaction.execute()

# Creating the Cash Dispenser class
class CashDispenser:
    def __init__(self, initial_cash):
        self.initial_cash = initial_cash
        self.lock = threading.Lock()
    
    # Creating the method for dispence cash
    def dispense_cash(self, amount):
        with self.lock:
            if amount > self.initial_cash:
                raise ValueError("Insufficient funds in the ATM")
            self.initial_cash -= amount
            print(f"Amount {amount} is withdrawn from the ATM")
        
# Creating the ATM class
class ATM:
    def __init__(self, banking_service, cash_dispenser):
        self.banking_service = banking_service
        self.cash_dispenser = cash_dispenser
        self.transaction_counter = 0
        self.transaction_lock = threading.Lock()
    
    # Creating the method for authenticating the user
    def authenticate_user(self, account):
        entered_pin = int(input("Enter 4 digit Pin: "))
        if account.verify_pin(entered_pin):
            print("Authentication Successful")
            return True
        else:
            print("Entered Pin is incorrect")
            return False
    
    # Creating the method for checking the balance
    def check_balance(self, account_number):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            print(f"Account Balance: ${account.get_balance():.2f}")
            return account.get_balance()
        else:
            print(f"Authentication Failed or Account not found")
            return None
    
    # Craeting the method for withdrawing the amount
    def withdraw_cash(self, account_number, amount):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            if account.get_balance() >= amount:
                transaction = WithdrawalTransaction(self.generate_transaction_id(), account, amount)
                self.banking_service.process_transaction(transaction)
                self.cash_dispenser.dispense_cash(int(amount))
                print(f"Withdrawal Successful !!!... Updated Balance: ${account.get_balance():.2f}")
            else:
                print(f"Insufficient funds in the account")
        else:
            print("Authentication Failed or Account not Found")

    # Craeting the method for deposit the amount
    def diposite_cash(self, account_number, amount):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            transaction = DepositeTransaction(self.generate_transaction_id(), account, amount)
            self.banking_service.process_transaction(transaction)
            print(f"Deposite Successful !!!... Updated Balance: ${account.get_balance():.2f}")
        else:
            print("Authentication Failed or Account not Found")
            
    # Creating the method for generating the Transaction ID
    def generate_transaction_id(self):
        self.transaction_counter += 1
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}{self.transaction_counter:0101d}"
    

# Creating the Main Function
if __name__ == "__main__":

    # Creating the object for Banking Service
    banking_service = BankingService()
    # Creating the object for cash dispenser
    cash_dispenser = CashDispenser(1000)

    # Creating the object for ATM
    atm = ATM(banking_service, cash_dispenser)

    # Creating the User accounts
    banking_service.create_account("1234567890", 1000.0, 1234)
    banking_service.create_account("0987654321", 2000.0, 4321)

    # Creating the Cards
    card_1 = Card("1234567890")
    card_2 = Card("0987654321")

    # Checking the balance for the user 1
    print("\nChecking the balance for User 1")
    atm.check_balance(card_1.get_card_number())

    # Withdrawing the amount from user1
    print("Withdrawing amount from User 1")
    atm.withdraw_cash(card_1.get_card_number(), 1000)

    # Checking the balance for the user 2
    print("\nChecking the balance for User 2")
    atm.check_balance(card_2.get_card_number())

    # Withdrawing the amount from user2
    print("Withdrawing amount from User 2")
    atm.withdraw_cash(card_2.get_card_number(), 1000)
