
### **System Overview – Why These Classes?**

The system is designed to **simulate an Amazon-style locker system**, where customers can **receive packages from couriers and later retrieve them using a PIN**. The key components of the system are:

1. **Locker** – Represents an individual storage unit for a package.
2. **Customer** – Represents a user who receives packages in lockers.
3. **AmazonLockerSystem** – The **centralized management system** that handles locker assignments.
4. **Location** – Represents a **physical location** where lockers are stored.

Each of these classes plays a critical role in **managing locker operations efficiently** while following **object-oriented principles** like **encapsulation, modularity, and the Singleton & Observer patterns**.

---

## **1️⃣ Locker Class (Represents a Single Locker)**

### **Why Do We Need It?**

A locker is the **core entity** in our system—it **holds the package and assigns it to a customer**. Each locker has **a unique ID, size, and status (occupied or available)**.

### **What Does This Class Do?**

This class **manages individual locker behavior**, including **assigning, locking, unlocking, and freeing up space**.

### **Functions Inside `Locker`**

- **`__init__`** → Initializes the locker with:
    
    - `locker_id`: A unique ID for each locker.
    - `size`: The size category (Small, Medium, Large).
    - `is_assigned`: Tracks whether the locker is occupied.
    - `pin`: A randomly generated PIN for package retrieval.
    - `assigned_customer`: The customer assigned to this locker.
- **`assign(self, customer, pin)`** → Assigns a locker to a customer with a **random PIN** and notifies them.
    
- **`free(self)`** → Clears the locker after the customer retrieves their package.
    
- **`check_pin(self, pin)`** → Verifies if the **correct PIN** is entered before unlocking.
    

### **How is it Used?**

Each **locker object is stored inside the `Location` class**, and we access these lockers when a customer **requests or retrieves a package**.

---

## **2️⃣ Customer Class (Represents a User)**

### **Why Do We Need It?**

A customer **places orders and retrieves packages**. They need to:

- **Receive notifications** when assigned a locker.
- **Track which locker they’ve been assigned**.
- **Enter the correct PIN to unlock a locker**.

### **What Does This Class Do?**

This class **manages customer interactions with the locker system**.

### **Functions Inside `Customer`**

- **`__init__`** → Creates a customer profile with a `customer_id` and keeps track of their assigned lockers (`assigned_lockers`).
    
- **`update(self, locker_id, pin)`** → When a **locker is assigned**, the system **notifies the customer** with the locker ID and PIN.
    
- **`remove_locker(self, locker_id)`** → When a **package is retrieved**, the locker assignment is removed from the customer’s list.
    
- **`order_package(self, package_size, amazon_locker_system, locker_id)`** → The customer **requests a locker** for their package.
    
- **`unassign_locker(self, locker_id, pin)`** → The customer **tries to unlock their locker** by entering the correct PIN.
    

### **How is it Used?**

- A **customer object** is created in `main()`.
- When they order a package, the `AmazonLockerSystem` **assigns a locker**.
- They receive a **notification with a PIN**.
- When they enter the **correct PIN**, the locker **unlocks**, and they retrieve the package.

---

## **3️⃣ AmazonLockerSystem (Manages Everything)**

### **Why Do We Need It?**

This class **acts as the "brain" of the system**, managing:

- **Locker assignments** (manual selection by the courier).
- **Verifying locker availability**.
- **Ensuring the correct package fits in the chosen locker**.
- **Unlocking lockers based on PIN authentication**.

This class follows the **Singleton Pattern**, meaning **only one instance** of this class **can exist in the entire program**.

### **What Does This Class Do?**

This class **handles the business logic** behind assigning, managing, and unlocking lockers.

### **Functions Inside `AmazonLockerSystem`**

- **`__new__`** → Implements the **Singleton Pattern** to ensure only one instance of `AmazonLockerSystem` exists.
    
- **`set_location(self, location)`** → Connects the **locker system** to a **physical location**.
    
- **`assign_locker(self, customer, package_size, locker_id)`** →
    
    - **Courier selects a locker**.
    - Checks if the **locker is available**.
    - **Validates package size compatibility**.
    - Assigns the locker and **generates a random PIN**.
- **`unlock_locker(self, customer, locker_id, pin)`** →
    
    - Verifies **if the PIN is correct**.
    - **Unlocks the locker** and frees it for future use.

### **How is it Used?**

- **Created as a Singleton** (`amazon_locker_system`).
- **Manages locker assignments and unlocking requests**.
- **Ensures all business rules are enforced** (e.g., large packages can’t be placed in small lockers).

---

## **4️⃣ Location Class (Represents the Physical Locker Station)**

### **Why Do We Need It?**

Since **lockers exist in a physical location**, we need a class to **group and manage lockers**.

### **What Does This Class Do?**

This class **creates and stores lockers** in predefined categories.

### **Functions Inside `Location`**

- **`__init__(self)`** → Creates **60 lockers**:
    - **20 Small lockers** (IDs 1-20).
    - **20 Medium lockers** (IDs 21-40).
    - **20 Large lockers** (IDs 41-60).

### **How is it Used?**

- **Instantiated in `main()`** as `location`.
- **Passed to `AmazonLockerSystem`** so it knows where the lockers exist.

---

## **How Do These Classes Work Together?**

### **Step-by-Step Flow**

1️⃣ The program **initializes the system**:

- `amazon_locker_system` (Singleton) is created.
- `location` (Physical storage for lockers) is initialized.

2️⃣ Customers **place orders manually**:

- `customer1.order_package(PackageSize.SMALL, amazon_locker_system, 5)`

3️⃣ **AmazonLockerSystem** checks:

- **Is locker 5 available?**
- **Does the package fit in the locker?**
- **If valid, assigns it & sends a PIN notification to customer1**.

4️⃣ **Customer retrieves package**:

- `customer1.unassign_locker(5, correct_PIN)`
- If PIN is correct, **locker is freed**.