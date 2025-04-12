
from abc import ABC, abstractmethod
#abc is an abstract base class module, ABC is a abstract base class.
# Abstract Pizza Class
class Pizza(ABC): #base abstract class is implement
    def __init__(self): #initi is a constructor of Pizza class
        self.description = "Unknown Pizza" #class variable

    def get_description(self): #class method
        return self.description

    @abstractmethod
    def get_cost(self):
        pass

# Concrete Pizza Classes (Base Pizzas)
class Margherita(Pizza):
    def __init__(self): #construc for marg pizza class 
        super().__init__() ##pizza constructopr wala init. it will be unknown pizza(parent class)
        self.description = "Margherita" #got the parent class i have now. but i am overriding inthis. desp is margetira.

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
    pizza2 = FreshTomato(pizza2)  # Adding Fresh Tomato
    pizza2 = FreshTomato(pizza2)
    pizza2 = Paneer(pizza2)  # Adding Paneer

    print(f"{pizza2.get_description()} - Cost: ${pizza2.get_cost()}")

    # Create a ChickenFiesta pizza and add Barbeque topping
    pizza3 = ChickenFiesta()
    pizza3 = Barbeque(pizza3)  # Adding Barbeque

    print(f"{pizza3.get_description()} - Cost: ${pizza3.get_cost()}")
