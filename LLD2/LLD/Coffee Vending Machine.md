## Requirements

1. The coffee vending machine should support different types of coffee, such as espresso, cappuccino, and latte.
2. Each type of coffee should have a specific price and recipe (ingredients and their quantities).
3. The machine should have a menu to display the available coffee options and their prices.
4. Users should be able to select a coffee type and make a payment.
5. The machine should dispense the selected coffee and provide change if necessary.
6. The machine should track the inventory of ingredients and notify when they are running low.
7. The machine should handle multiple user requests concurrently and ensure thread safety.

## Classes, Interfaces and Enumerations

1. The **Coffee** class represents a coffee type with its name, price, and recipe (ingredients and their quantities).
2. The **Ingredient** class represents an ingredient used in making coffee, with its name and quantity. It provides a synchronized method to update the quantity.
3. The **Payment** class represents a payment made by a user, with the amount paid.
4. The **CoffeeMachine** class is the main class that manages the coffee vending machine. It follows the Singleton pattern to ensure a single instance of the machine.
5. The **CoffeeMachine** class initializes the coffee menu and ingredients in its constructor. It provides methods to display the menu, select a coffee, dispense coffee, and update ingredient quantities.
6. The hasEnoughIngredients method checks if there are sufficient ingredients to make a selected coffee, while the updateIngredients method updates the ingredient quantities after dispensing a coffee.
7. The **CoffeeVendingMachine** class is the entry point of the application and demonstrates the usage of the coffee vending machine. It creates an instance of the machine, displays the menu, and simulates concurrent user requests using an ExecutorService.


---

#### **Overview of the Coffee Vending Machine System**

This system is designed to simulate a real-world **coffee vending machine** that allows users to purchase different types of coffee. The machine manages **ingredients**, **coffee menu**, **payments**, and ensures **inventory tracking**. It implements object-oriented principles and follows key software design patterns.

---

## **Design Patterns and Principles Used**

1. **Singleton Design Pattern**:
    
    - The `CoffeeMachine` class follows the **Singleton Pattern**, ensuring that only one instance of the coffee vending machine exists in the system.
    - This is useful because a real-world coffee machine is a **single entity**, meaning there shouldn't be multiple instances of the machine running in a single system.
    - This is enforced using the `_instance` attribute and the `get_instance()` method, which ensures that only one object of `CoffeeMachine` is created.
2. **Encapsulation and Abstraction**:
    
    - **Encapsulation**:
        - Each class is **self-contained**, meaning that data (attributes) and behaviors (methods) that operate on that data are grouped together.
        - For example, the `Ingredient` class has methods like `get_quantity()` and `update_quantity()` which ensure that external classes **do not directly modify** the ingredient quantities.
    - **Abstraction**:
        - The **user** interacts with the `CoffeeMachine` through a limited set of methods (`display_menu()`, `select_coffee()`, and `dispense_coffee()`), without knowing how the coffee is actually dispensed.
        - The complexity of **checking ingredients, calculating payments, and updating inventory** is hidden inside the `CoffeeMachine` class.
3. **SOLID Principles Applied**
    
    - **Single Responsibility Principle (SRP)**:
        - Each class has **one responsibility**:
            - `Coffee` stores coffee details.
            - `Ingredient` manages ingredients and their quantities.
            - `Payment` handles payment transactions.
            - `CoffeeMachine` manages coffee selection, inventory, and dispensing.
    - **Open/Closed Principle (OCP)**:
        - The system can be **extended** without modifying existing classes.
        - If a new type of coffee is introduced, we just **add it to the menu**, without changing other logic.
    - **Liskov Substitution Principle (LSP)**:
        - If we wanted to add a **new type of payment method** (e.g., Card Payments), we could create a subclass of `Payment` without modifying the existing system.
    - **Dependency Inversion Principle (DIP)**:
        - The `CoffeeMachine` does not directly depend on **specific coffee types**; instead, it depends on an abstract list of coffee objects.

---

## **Class-by-Class Breakdown**

Now, let's go through each class in detail and explain **why we created it** and **how it relates to other classes**.

### **1. Ingredient Class**

The `Ingredient` class represents **individual ingredients** used in coffee making, like Coffee Powder, Water, and Milk.

- It encapsulates **ingredient name and available quantity**.
- The `update_quantity()` method allows controlled modification of ingredient stock.

🔹 **Why is this class needed?**

- Instead of hardcoding ingredients inside the `CoffeeMachine`, we store them as **objects**, making it easier to manage and extend.

🔹 **How does it relate to other classes?**

- `CoffeeMachine` maintains a **collection of ingredients**, which is updated when a coffee is made.

---

### **2. Coffee Class**

The `Coffee` class defines a **specific coffee type**, such as **Espresso, Cappuccino, or Latte**.

- It contains a **name, price, and recipe** (i.e., how much of each ingredient is needed).
- Recipes are stored as **dictionaries mapping ingredients to required quantities**.

🔹 **Why is this class needed?**

- Instead of treating coffee types as simple names, we represent them as **objects** with structured data.
- This makes it easy to **add new coffee types** dynamically.

🔹 **How does it relate to other classes?**

- `CoffeeMachine` **stores a list of coffee objects** and retrieves them when a user selects a coffee.

---

### **3. Payment Class**

The `Payment` class represents a **payment transaction** by the user.

- It only stores the **amount paid** by the user.

🔹 **Why is this class needed?**

- This abstraction allows us to **extend payment functionality later**.
- For example, we could add `CardPayment` or `MobilePayment` as subclasses.

🔹 **How does it relate to other classes?**

- `CoffeeMachine` checks the `Payment` amount against the `Coffee` price before dispensing coffee.

---

### **4. CoffeeMachine Class (Singleton)**

The `CoffeeMachine` class is the **core of the system**.

- It follows the **Singleton Pattern**, ensuring **only one machine** exists.
- It **initializes ingredients and coffee menu**, and provides methods to:
    1. Display the menu.
    2. Select a coffee.
    3. Dispense coffee (if enough ingredients are available).

🔹 **Why is this class needed?**

- It serves as the **controller** that manages the vending process.
- Without this, we’d have **scattered logic across multiple places**.

🔹 **How does it relate to other classes?**

- It **stores and modifies ingredients**.
- It **manages coffee objects** and retrieves the recipe when a coffee is selected.
- It **checks payments** before dispensing coffee.

---

### **5. Coffee Vending Machine Execution (`__main__` Block)**

This section **creates the machine instance** and **simulates user interactions**.

- First, the **coffee menu is displayed**.
- Then, **users select and purchase coffee**.

🔹 **Where are objects created and initialized?**

- `CoffeeMachine.get_instance()` creates the **singleton instance** of the machine.
- Ingredients (`Ingredient`) and coffee types (`Coffee`) are initialized inside `CoffeeMachine`.
- `Payment` objects are created dynamically when a user pays.

---

## **System Flow Explanation**

Now, let’s understand how the system **executes step-by-step**:

1. **Initialization**:
    
    - `CoffeeMachine` **creates and stores** available ingredients.
    - It **populates the menu** with predefined coffee types.
2. **Displaying the Menu**:
    
    - The user sees a list of **coffee options and prices**.
3. **User Selects Coffee**:
    
    - The machine **retrieves the coffee object** from the menu.
4. **Payment Verification**:
    
    - The machine **compares** the amount paid with the coffee price.
5. **Checking Ingredient Availability**:
    
    - The system **ensures** that required ingredients are available.
6. **Dispensing Coffee**:
    
    - If conditions are met, the coffee is dispensed.
    - Ingredients **are updated**, and a **low inventory alert** is triggered if stock is below 3.
7. **Providing Change**:
    
    - If the user **paid extra**, change is returned.

---

## **Example Execution**

Let’s say a user selects **Cappuccino** and pays **$3.5**.

1. The machine verifies the **payment**.
2. It checks if **enough ingredients** are available.
3. It **deducts ingredient quantities** from inventory.
4. It **dispenses Cappuccino** and returns **change if applicable**.

If another user now tries to order **Latte**, but **Milk is running low**, the machine **alerts the operator**.

```
class Ingredient:

    def __init__(self, name, quantity):

        self.name = name

        self.quantity = quantity

  

    def get_name(self):

        return self.name

  

    def get_quantity(self):

        return self.quantity

  

    def update_quantity(self, amount):

        self.quantity += amount

  
  

class Coffee:

    def __init__(self, name, price, recipe):

        self.name = name

        self.price = price

        self.recipe = recipe

  

    def get_name(self):

        return self.name

  

    def get_price(self):

        return self.price

  

    def get_recipe(self):

        return self.recipe

  
  

class Payment:

    def __init__(self, amount):

        self.amount = amount

  

    def get_amount(self):

        return self.amount

  
  

class CoffeeMachine:

    _instance = None

  

    def __init__(self):

        if CoffeeMachine._instance is not None:

            raise Exception("This class is a singleton!")

        else:

            CoffeeMachine._instance = self

            self.coffee_menu = []

            self.ingredients = {}

            self._initialize_ingredients()

            self._initialize_coffee_menu()

  

    @staticmethod

    def get_instance():

        if CoffeeMachine._instance is None:

            CoffeeMachine()

        return CoffeeMachine._instance

  

    def _initialize_coffee_menu(self):

        espresso_recipe = {

            self.ingredients["Coffee"]: 1,

            self.ingredients["Water"]: 1

        }

        self.coffee_menu.append(Coffee("Espresso", 2.5, espresso_recipe))

  

        cappuccino_recipe = {

            self.ingredients["Coffee"]: 1,

            self.ingredients["Water"]: 1,

            self.ingredients["Milk"]: 1

        }

        self.coffee_menu.append(Coffee("Cappuccino", 3.5, cappuccino_recipe))

  

        latte_recipe = {

            self.ingredients["Coffee"]: 1,

            self.ingredients["Water"]: 1,

            self.ingredients["Milk"]: 2

        }

        self.coffee_menu.append(Coffee("Latte", 4.0, latte_recipe))

  

    def _initialize_ingredients(self):

        self.ingredients["Coffee"] = Ingredient("Coffee", 10)

        self.ingredients["Water"] = Ingredient("Water", 10)

        self.ingredients["Milk"] = Ingredient("Milk", 10)

  

    def display_menu(self):

        print("\n☕ Coffee Menu:")

        for coffee in self.coffee_menu:

            print(f"{coffee.get_name()} - ${coffee.get_price()}")

  

    def select_coffee(self, coffee_name):

        for coffee in self.coffee_menu:

            if coffee.get_name().lower() == coffee_name.lower():

                return coffee

        return None

  

    def dispense_coffee(self, coffee, payment):

        if not coffee:

            print("❌ Coffee not found in the menu.")

            return

  

        if payment.get_amount() >= coffee.get_price():

            if self._has_enough_ingredients(coffee):

                self._update_ingredients(coffee)

                print(f"\n✅ Dispensing {coffee.get_name()}...")

                change = payment.get_amount() - coffee.get_price()

                if change > 0:

                    print(f"💰 Please collect your change: ${change:.2f}")

                else:

                    print("Payment Successful !!! Enjoy your coffee ☕")

            else:

                print(f"❌ Insufficient ingredients to make {coffee.get_name()}")

        else:

            print(f"❌ Insufficient payment for {coffee.get_name()}")

  

    def _has_enough_ingredients(self, coffee):

        for ingredient, required_quantity in coffee.get_recipe().items():

            if ingredient.get_quantity() < required_quantity:

                return False

        return True

  

    def _update_ingredients(self, coffee):

        for ingredient, required_quantity in coffee.get_recipe().items():

            ingredient.update_quantity(-required_quantity)

            if ingredient.get_quantity() < 3:

                print(f"⚠️ Low inventory alert: {ingredient.get_name()}")

  
  

if __name__ == "__main__":

    coffee_machine = CoffeeMachine.get_instance()

  

    # Display coffee menu

    coffee_machine.display_menu()

  

    # Simulate user requests

    espresso = coffee_machine.select_coffee("Espresso")

    coffee_machine.dispense_coffee(espresso, Payment(3.0))

  

    cappuccino = coffee_machine.select_coffee("Cappuccino")

    coffee_machine.dispense_coffee(cappuccino, Payment(3.5))

  

    latte = coffee_machine.select_coffee("Latte")

    coffee_machine.dispense_coffee(latte, Payment(4.0))
```