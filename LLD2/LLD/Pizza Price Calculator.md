``
![[Pasted image 20250203154459.jpg]]

In this **Pizza Shop System**, we use the **Decorator Pattern** to allow customers to customize their pizzas by adding toppings dynamically.

---

## **1️⃣ Classes in the System and Their Purpose**

The system consists of **four main types of classes**:

1. **Abstract Base Class (`Pizza`)** - Defines a pizza's common properties and behavior.
2. **Concrete Pizzas (`Margherita`, `FarmHouse`, etc.)** - Specific types of pizzas with base prices.
3. **Abstract Decorator (`ToppingDecorator`)** - Acts as a wrapper to extend pizza functionality.
4. **Concrete Toppings (`FreshTomato`, `Paneer`, etc.)** - Extend the `ToppingDecorator` to modify the base pizza.

---

## **2️⃣ Why These Classes?**

- **To Separate Concerns**:
    - The `Pizza` class handles core pizza functionality.
    - The `ToppingDecorator` ensures toppings are independent and reusable.
    - `Concrete Pizzas` provide different types of pizzas.
    - `Concrete Toppings` allow easy addition of toppings dynamically.
- **To Follow Open/Closed Principle (OCP)**:
    - The system is **open for extension but closed for modification**.
    - We can add **new toppings without modifying existing pizza classes**.

---
### **📌 How Classes Are Related**

1. **`Pizza` (Abstract Base Class)**
    
    - Defines the blueprint for all pizzas.
    - Has `get_cost()` and `get_description()` methods.
    - **Concrete pizzas** extend `Pizza`.
2. **Concrete Pizzas (`Margherita`, `FarmHouse`, etc.)**
    
    - Extend `Pizza`.
    - Set their **own descriptions** and **base prices**.
3. **`ToppingDecorator` (Abstract Decorator Class)**
    
    - Extends `Pizza` **(so toppings can act like pizzas).**
    - **Has a reference to another `Pizza` object** (wrapping the base pizza).
    - Forces concrete decorators (`FreshTomato`, `Paneer`, etc.) to **override `get_cost()` and `get_description()`**.
4. **Concrete Toppings (`FreshTomato`, `Paneer`, etc.)**
    
    - Extend `ToppingDecorator`.
    - Modify the `Pizza` object they wrap.
    - Call `pizza.get_cost()` to add their price.

---
## **4️⃣ Why Use Abstraction?**

### **📌 Why Abstract Base Class (`Pizza`)?**

1. **Prevents Instantiation of Generic Pizzas**
    - A pizza **must** be of a specific type (Margherita, FarmHouse, etc.).
2. **Forces Consistency**
    - Ensures every pizza has `get_cost()` and `get_description()`.
3. **Allows Extension**
    - New pizzas can be added without modifying existing classes.

### **📌 Why Use `ToppingDecorator` as an Abstract Class?**

1. **Extends `Pizza` for Interchangeability**
    - Since it **inherits `Pizza`**, toppings can **wrap around pizzas**.
2. **Encapsulates the Base Pizza Object**
    - Ensures toppings **modify only the wrapped pizza object**.
3. **Prevents Direct Instantiation**
    - `ToppingDecorator` cannot be instantiated alone.

---

## **5️⃣ Why Not Use Interfaces Instead of Abstract Classes?**

**Python doesn’t have interfaces like Java, but we could have used composition.**  
However, **abstract classes are better** because:

1. **We Can Provide a Default Implementation**
    - The `Pizza` class **has a default `description`**.
2. **Prevents Unnecessary Implementations**
    - We don’t need every concrete pizza to redefine `get_description()`.
3. **Ensures `ToppingDecorator` is Treated Like a Pizza**
    - If `ToppingDecorator` was an interface, toppings wouldn’t be interchangeable with pizzas.

```
from abc import ABC, abstractmethod


# Abstract Pizza Class
class Pizza(ABC):
    def __init__(self):
        self.description = "Unknown Pizza"

    def get_description(self):
        return self.description

    @abstractmethod
    def get_cost(self):
        pass

# Concrete Pizza Classes (Base Pizzas)
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita"

    def get_cost(self):
        return 100

class FarmHouse(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "FarmHouse"

    def get_cost(self):
        return 200

  
class ChickenFiesta(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "ChickenFiesta"
  
    def get_cost(self):
        return 200

class SimplePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Simple Pizza"

    def get_cost(self):
        return 50


# Abstract Decorator Class
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

  
# Concrete Topping Decorators
class FreshTomato(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Fresh Tomato"

    def get_cost(self):
        return self.pizza.get_cost() + 40

  
class Barbeque(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Barbeque"

    def get_cost(self):
        return self.pizza.get_cost() + 90

  
class Paneer(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Paneer"

    def get_cost(self):
        return self.pizza.get_cost() + 70

  

# Main Function (Driver Code)
if __name__ == "__main__":

    # Create a plain Margherita pizza
    pizza1 = Margherita()
    print(f"{pizza1.get_description()} - Cost: ${pizza1.get_cost()}")


    # Create a FarmHouse pizza and add toppings dynamically
    pizza2 = FarmHouse()
    pizza2 = FreshTomato(pizza2)  # Adding Fresh Tomato
    pizza2 = FreshTomato(pizza2)
    pizza2 = Paneer(pizza2)  # Adding Paneer
    print(f"{pizza2.get_description()} - Cost: ${pizza2.get_cost()}")

  
    # Create a ChickenFiesta pizza and add Barbeque topping
    pizza3 = ChickenFiesta()
    pizza3 = Barbeque(pizza3)  # Adding Barbeque
    print(f"{pizza3.get_description()} - Cost: ${pizza3.get_cost()}")
```