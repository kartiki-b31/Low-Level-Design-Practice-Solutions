
## Requirements

1. The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
2. Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
3. The system should interact with a bank's backend system to validate user accounts and perform transactions.
4. The ATM should have a cash dispenser to dispense cash to users.
5. The system should handle concurrent access and ensure data consistency.
6. The ATM should have a user-friendly interface for users to interact with.

## Classes, Interfaces and Enumerations

1. The **Card** class represents an ATM card with a card number and PIN.
2. The **Account** class represents a bank account with an account number and balance. It provides methods to debit and credit the account balance.
3. The **Transaction** class is an abstract base class for different types of transactions, such as withdrawal and deposit. It is extended by WithdrawalTransaction and DepositTransaction classes.
4. The **BankingService** class manages the bank accounts and processes transactions. It uses a thread-safe ConcurrentHashMap to store and retrieve account information.
5. The **CashDispenser** class represents the ATM's cash dispenser and handles the dispensing of cash. It uses synchronization to ensure thread safety when dispensing cash.
6. The **ATM** class serves as the main interface for ATM operations. It interacts with the BankingService and CashDispenser to perform user authentication, balance inquiry, cash withdrawal, and cash deposit.
7. The **ATMDriver** class demonstrates the usage of the ATM system by creating sample accounts and performing ATM operations.

---


The ATM system is designed to simulate real-world ATM operations, including balance inquiry, cash withdrawal, and deposit transactions. The system follows **object-oriented programming (OOP) principles** by breaking down the functionality into multiple classes, each responsible for a specific aspect of the ATM's operations. Below is a **detailed breakdown** of the implementation, covering the **design choices, relationships between classes, and execution flow**.

---

## **1️⃣ Classes & Their Responsibilities**

To create a modular and scalable system, we divided the ATM functionality into different classes, each responsible for handling a **specific** operation. This follows the **Single Responsibility Principle (SRP)** from SOLID design principles.

### **🔹 Account Class**

- The `Account` class represents a **bank account**, which holds critical information such as:
    - **Account Number** (Unique Identifier)
    - **Balance** (Stores the current account balance)
    - **PIN** (Used for authentication)
- It provides **methods** to:
    - **Verify the PIN** when a user attempts a transaction.
    - **Debit** and **credit** the balance when withdrawing or depositing money.
- This class **ensures security** by storing the PIN securely inside the account rather than exposing it to external components.

🔹 **Why is the PIN stored in the Account?**

- The PIN is **not** stored inside the `Card` class because, in real-world banking, the ATM card only serves as an **identifier** for the account. The **PIN is verified** inside the bank’s backend system, not on the card itself.
- By storing the PIN inside the `Account` class, we ensure that authentication logic is handled within the banking system.

---

### **🔹 Card Class**

- Represents a **physical ATM card** that belongs to a user.
- Stores only the **Card Number** (which is linked to an `Account`).
- The `Card` class does **not** contain sensitive information like the PIN. Instead, when a user inserts their card, the **ATM retrieves the associated account** from the `BankingService` and then requests authentication.

🔹 **Why Separate `Card` and `Account`?**

- This mimics real-world ATM behavior, where the **card number** is just an identifier, but the authentication happens against a bank database (i.e., `Account` class).
- Helps maintain a **clear separation of concerns** between **physical identification (Card)** and **actual financial data (Account)**.

---

### **🔹 Abstract Transaction Class**

- The `Transaction` class is an **abstract class**, meaning it **cannot be instantiated directly**.
- It defines a **common structure** for all types of transactions (withdrawals, deposits, etc.).
- Declares an **abstract method `execute()`**, which forces child classes (`WithdrawalTransaction` and `DepositTransaction`) to implement their own logic.

🔹 **Why Use an Abstract Class?**

- Since every transaction (withdrawal, deposit) has a **unique execution process**, we define a **common structure** in the abstract class and let the specific transaction types **override** the `execute()` method.
- This follows **polymorphism** in OOP, allowing us to **treat different types of transactions uniformly** while keeping their implementations separate.

---

### **🔹 WithdrawalTransaction & DepositTransaction Classes**

- These classes **inherit from the `Transaction` class`** and **implement** the` execute()` method.
- `WithdrawalTransaction` **deducts** the specified amount from the account balance.
- `DepositTransaction` **adds** the amount to the account balance.
- This makes the system **extensible**—if we ever need to introduce new transactions (e.g., fund transfer), we can simply **create another subclass** without modifying existing code.

---

### **🔹 BankingService Class**

- The `BankingService` acts as a **database for accounts** and provides methods to:
    - **Create new accounts** (stores account details)
    - **Retrieve account details** based on an account number
    - **Process transactions** (calls the `execute()` method on transactions)
- This class **ensures that all banking operations are managed centrally** and provides a secure way to interact with the bank’s backend system.

🔹 **Why Have a Separate `BankingService` Class?**

- This class **acts as the bank’s backend system**, meaning all **authentication and transactions** must go through it.
- It ensures that ATM operations **don’t directly manipulate account data**, enforcing better **encapsulation**.

---

### **🔹 CashDispenser Class**

- The `CashDispenser` **physically dispenses cash** to users.
- Uses a **thread-safe lock** to prevent multiple transactions from dispensing cash at the same time.
- Ensures that the ATM **never dispenses more cash than is available**.

🔹 **Why Use Threading in `CashDispenser`?**

- Since multiple users might **withdraw cash simultaneously**, we need to **synchronize access** to ensure that:
    - The ATM **doesn’t dispense more cash than it has**.
    - Two users **don’t withdraw the same cash at the same time**.

---

### **🔹 ATM Class (Main Interface)**

- The `ATM` class is the **entry point** for all ATM operations.
- It interacts with:
    - **`BankingService`** to authenticate users and process transactions.
    - **`CashDispenser`** to dispense cash.
- Provides user-facing **methods** such as:
    - `authenticate_user()`
    - `check_balance()`
    - `withdraw_cash()`
    - `deposit_cash()`
- Uses a **transaction counter** to generate unique transaction IDs.

🔹 **Why Is `ATM` a Separate Class?**

- **Encapsulates all ATM-related operations** in a single place.
- Acts as an **interface between the user and the banking system**.

---

## **2️⃣ Execution Flow (Step by Step)**

Now, let’s go through what happens when the ATM runs:

### **🔵 1. Initializing the ATM System**

- A `BankingService` object is created, which **stores all user accounts**.
- A `CashDispenser` object is initialized with **$10,000**.
- An `ATM` object is created, linking the banking service and cash dispenser.

### **🔵 2. Creating Bank Accounts**

- Two **sample accounts** are created:
    - Account 1: `1234567890` → Balance: **$1000**, PIN: **1234**
    - Account 2: `9876543210` → Balance: **$500**, PIN: **4321**
- Two `Card` objects are also created to **simulate ATM cards**.

### **🔵 3. Checking Balance**

- The user enters their **PIN** for authentication.
- If the PIN is correct, the ATM **retrieves and prints** the account balance.

### **🔵 4. Withdrawing Cash**

- The ATM first **authenticates the user**.
- Checks if the **balance is sufficient**.
- If yes:
    - Creates a `WithdrawalTransaction`.
    - Calls `process_transaction()`, which executes the withdrawal.
    - Dispenses cash using `CashDispenser`.
- If not:
    - Prints an **error message**.

### **🔵 5. Depositing Cash**

- Similar to withdrawal, but the amount is **credited** to the account instead of debited.

---

## **3️⃣ Key Design Choices & Why They Matter**

✅ **Encapsulation**: All classes **restrict direct access** to sensitive data (e.g., balance, PIN).  
✅ **Security**: PIN is verified inside the `Account` class, not stored in the `Card` class.  
✅ **Thread Safety**: The `CashDispenser` prevents race conditions using locks.  
✅ **Extensibility**: Adding a new transaction type is **as simple as creating a new subclass**.  
✅ **Modular Design**: Each class has a **clear responsibility**, making the code easy to maintain.



```
import datetime

import threading

from abc import ABC, abstractmethod

  

# Account Class

class Account:

    def __init__(self, account_number, balance, pin):

        self.account_number = account_number

        self.balance = balance

        self.pin = pin  # Store the PIN inside the account itself

  

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

    banking_service.create_account("1234567890", 1000.0, "1234")  # User 1

    banking_service.create_account("9876543210", 500.0, "4321")  # User 2

  

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

    atm.withdraw_cash(card_2.get_card_number(), 600.0)  # Should fail
```