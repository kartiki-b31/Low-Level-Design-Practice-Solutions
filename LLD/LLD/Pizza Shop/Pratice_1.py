# Predefined Pizzas - Yes, Mergherita, FarmHouse, DoubleCheese, Cheese
# Toppings Yes - Tomato, Pepper, Olives, Corn, Chicken, Ham

from abc import ABC, abstractmethod
# Creating the base Pizza Class
class Pizza(ABC):
    def __init__(self):
        self.pizza_description = "Unknown Pizza"

    # Creating the get_description method
    def get_description(self):
        return self.pizza_description
    
    # Creating the get_cost method
    def get_cost(self):
        pass

# Creating the Concrete Pizza Classes
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_description = "Margherita Pizza"
    
    # creating the get_cost method
    def get_cost(self):
        return 3

class FarmHouse(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_description = "FarmHouse Pizza"
    
    # creating the get_cost method
    def get_cost(self):
        return 4

class DoubleCheese(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_description = "DoubleCheese Pizza"
    
    # creating the get_cost method
    def get_cost(self):
        return 2

class Cheese(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_description = "Cheese Pizza"
    
    # creating the get_cost method
    def get_cost(self):
        return 1.5

# Creating the Abstract Topping Decorator Class
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza
    
    # Creating the get_description method
    def get_description(self):
        pass

    # Creating the get_cost method
    def get_cost(self):
        pass

# Creating the Concrete Topping Decorators
class Tomato(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Tomato"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5

class Pepper(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Pepper"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5
    
class Olives(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5
    
class Corn(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Corn"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5

class Chicken(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Chicken"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5

class Ham(ToppingDecorator):
    def get_description(self):
        return self.pizza.get_description() + ", Ham"

    # Creating the get_cost method
    def get_cost(self):
        return self.pizza.get_cost() + 0.5

# Creating the Main Function
if __name__ == "__main__":

    # Creating the Pizza classes

    pizza_1 = Margherita()
    pizza_1 = Tomato(pizza_1)
    pizza_1 = Chicken(pizza_1)
    pizza_1 = Ham(pizza_1)

    print(f"Description \n{pizza_1.get_description()}\nCost : ${pizza_1.get_cost()}")

    pizza_2 = DoubleCheese()
    pizza_2 = Tomato(pizza_2)
    pizza_2 = Chicken(pizza_2)
    pizza_2 = Chicken(pizza_2)
    pizza_2 = Chicken(pizza_2)
    pizza_2 = Chicken(pizza_2)
    pizza_2 = Ham(pizza_2)

    print(f"Description \n{pizza_2.get_description()}\nCost : ${pizza_2.get_cost()}")