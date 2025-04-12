import datetime
import threading
from abc import ABC, abstractmethod

# Account Class
class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin  # Store the PIN inside the account itself

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount


# Card Class
class Card:
    def __init__(self, card_number):
        self.card_number = card_number

    def get_card_number(self):
        return self.card_number


# Abstract Transaction Class
class Transaction(ABC):
    def __init__(self, transaction_id, account, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount

    @abstractmethod
    def execute(self):
        pass


# Withdrawal Transaction
class WithdrawalTransaction(Transaction):
    def __init__(self, transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)

    def execute(self):
        self.account.debit(self.amount)


# Deposit Transaction
class DepositTransaction(Transaction):
    def __init__(self, transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)

    def execute(self):
        self.account.credit(self.amount)


# Banking Service
class BankingService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance, pin):
        self.accounts[account_number] = Account(account_number, initial_balance, pin)

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def process_transaction(self, transaction):
        transaction.execute()


# Cash Dispenser
class CashDispenser:
    def __init__(self, initial_cash):
        self.cash_available = initial_cash
        self.lock = threading.Lock()

    def dispense_cash(self, amount):
        with self.lock:
            if amount > self.cash_available:
                raise ValueError("Insufficient cash available in the ATM.")
            self.cash_available -= amount
            print("💰 Cash dispensed:", amount)


# ATM Class
class ATM:
    def __init__(self, banking_service, cash_dispenser):
        self.banking_service = banking_service
        self.cash_dispenser = cash_dispenser
        self.transaction_counter = 0
        self.transaction_lock = threading.Lock()

    def authenticate_user(self, account):
        """ Authenticate user by verifying their PIN """
        entered_pin = input("🔑 Enter your PIN: ")
        if account.verify_pin(entered_pin):
            print("✅ Authentication Successful")
            return True
        else:
            print("❌ Authentication Failed: Incorrect PIN")
            return False

    def check_balance(self, account_number):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            print(f"💳 Account Balance: ${account.get_balance():.2f}")
            return account.get_balance()
        print("❌ Authentication Failed or Account Not Found")
        return None

    def withdraw_cash(self, account_number, amount):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            if account.get_balance() >= amount:
                transaction = WithdrawalTransaction(self.generate_transaction_id(), account, amount)
                self.banking_service.process_transaction(transaction)
                self.cash_dispenser.dispense_cash(int(amount))
                print(f"✅ Withdrawal Successful. Updated Balance: ${account.get_balance():.2f}")
            else:
                print("❌ Insufficient funds.")
        else:
            print("❌ Authentication Failed or Account Not Found")

    def deposit_cash(self, account_number, amount):
        account = self.banking_service.get_account(account_number)
        if account and self.authenticate_user(account):
            transaction = DepositTransaction(self.generate_transaction_id(), account, amount)
            self.banking_service.process_transaction(transaction)
            print(f"✅ Deposit Successful. Updated Balance: ${account.get_balance():.2f}")
        else:
            print("❌ Authentication Failed or Account Not Found")

    def generate_transaction_id(self):
        with self.transaction_lock:
            self.transaction_counter += 1
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            return f"TXN{timestamp}{self.transaction_counter:010d}"


# ATM Demo Execution
if __name__ == "__main__":
    banking_service = BankingService()
    cash_dispenser = CashDispenser(10000)
    atm = ATM(banking_service, cash_dispenser)

    # Create sample accounts
    banking_service.create_account("1234567890", 1000.0, "1234")  # User 1
    banking_service.create_account("9876543210", 500.0, "4321")  # User 2

    # Create cards
    card_1 = Card("1234567890")
    card_2 = Card("9876543210")

    # Perform ATM operations
    print("\n🔵 Checking Balance for User 1:")
    atm.check_balance(card_1.get_card_number())

    print("\n🔵 Withdrawing Cash for User 1:")
    atm.withdraw_cash(card_1.get_card_number(), 500.0)

    print("\n🔵 Checking Updated Balance for User 1:")
    atm.check_balance(card_1.get_card_number())

    print("\n🔵 Depositing Cash for User 2:")
    atm.deposit_cash(card_2.get_card_number(), 200.0)

    print("\n🔵 Checking Balance for User 2:")
    atm.check_balance(card_2.get_card_number())

    print("\n🔵 Withdrawing Cash for User 2 (More than balance to test failure):")
    atm.withdraw_cash(card_2.get_card_number(), 600.0)  # Should fail
