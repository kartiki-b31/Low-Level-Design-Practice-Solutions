# # Pizza Class - Blueprint of all the pizzas
# # Concrete Pizza Classes- This extend the Pizza class and based on the different Pizzas, they set their own name and value
# # Topping Decorator Class - This is the abstract class which extends the Pizza class and has a reference to the Pizza class
# # Concrete Topping Decorator Classes - These extend the Topping Decorator class and override the cost and description

# # We import Abstract Method from ABC module
# from abc import ABC, abstractmethod

# # Creating the Abstract Pizza Class
# class Pizza(ABC):
#     def __init__(self):
#         self.description = "Unknow Pizza"

#     def get_description(self):
#         return self.description
    
#     # Creating the Abstract Method
#     @abstractmethod
#     def get_cost(self):
#         pass

# # Creating the Concrete Pizza Classes
# class Margherita(Pizza):
#     def __init__(self):
#         super().__init__()
#         self.description = "Margeherita Pizza"
    
#     def get_cost(self):
#         return 2

# class FarmHouse(Pizza):
#     def __init__(self):
#         super().__init__()
#         self.description = "FarmHouse Pizza"
    
#     def get_cost(self):
#         return 3

# class Cheese(Pizza):
#     def __init__(self):
#         super().__init__()
#         self.description = "CHeese Pizza"
    
#     def get_cost(self):
#         return 1

# class DoubleCheese(Pizza):
#     def __init__(self):
#         super().__init__()
#         self.description = "Double Cheese Pizza"
    
#     def get_cost(self):
#         return 1.5

# # Creating the Abstract Topping Decorator Class
# class ToppingDecorator(Pizza):
#     def __init__(self, pizza):
#         super().__init__()
#         self.pizza = pizza
    
#     @abstractmethod
#     def get_description(self):
#         pass

#     @abstractmethod
#     def get_cost(self):
#         pass

# # Creating the concrete classes for Topping Decorator Class
# class Olives(ToppingDecorator):
#     def get_description(self):
#         return self.pizza.get_description() + ", Olives"
    
#     def get_cost(self):
#         return self.pizza.get_cost() + 0.3
    
# class Ham(ToppingDecorator):
#     def get_description(self):
#         return self.pizza.get_description() + ", Ham"
    
#     def get_cost(self):
#         return self.pizza.get_cost() + 0.5
    
# class Corn(ToppingDecorator):
#     def get_description(self):
#         return self.pizza.get_description() + ", Corn"
    
#     def get_cost(self):
#         return self.pizza.get_cost() + 0.1
    
# class Chicken(ToppingDecorator):
#     def get_description(self):
#         return self.pizza.get_description() + ", Chicken"
    
#     def get_cost(self):
#         return self.pizza.get_cost() + 0.4

# # Creating the Concrete Pizza Object
# if __name__ == "__main__":

#     # Creating the concrete Pizza object
#     pizza_1 = Margherita()
#     print(f"Description: {pizza_1.get_description()}, and Cost: {pizza_1.get_cost()}")

#     # Creating the Farmhouse pizza with toppings
#     pizza_2 = FarmHouse()
#     pizza_2 = Olives(pizza_2)
#     pizza_2 = Ham(pizza_2)
#     pizza_2 = Chicken(pizza_2)
#     pizza_2 = Corn(pizza_2)
#     print(f"Desciption : {pizza_2.get_description()}, and Cost : {pizza_2.get_cost()}")

# -------------------------------------------------------------------------------------------------------

# Requirement Gathering:
# 1 - Pizza Class will be the Blueprint of all the concrete pizza classes
# 2 - Types of Concrete Pizza classes -> Margherita, FarmHouse, DoubleCheese
# 3 - Topping Class
# 4 - Concrete Topping Class, extends the Topping Class, Olives, Chiken, Corn

from abc import ABC, abstractmethod

# Creating hte main Pizza Class
class Pizza(ABC):
    # Creating a Constructor with initiatling the name of Pizza
    def __init__(self):
        self.description = "Unkown Pizza"
    
    # Here we can also have a function that returns the description on Pizza
    def get_description(self,):
        return self.description

    # We create an abstract function that returns the total bill of the order
    @abstractmethod
    def get_cost(self,):
        pass

# Now lets create the concrete classes of Pizza 
class Margherita(Pizza):
    # Here we need to override the name of the main pizza class
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"

    # We create the cost function for this Pizza
    def get_cost(self):
        return 4

class FarmHouse(Pizza):
    # Here we need to override the name of the main pizza class
    def __init__(self):
        super().__init__()
        self.description = "FarmHouse Pizza"

    # We create the cost function for this Pizza
    def get_cost(self):
        return 3
        
class DoubleCheese(Pizza):
    # Here we need to override the name of the main pizza class
    def __init__(self):
        super().__init__()
        self.description = "DoubleCheese Pizza"

    # We create the cost function for this Pizza
    def get_cost(self):
        return 2

# Next we will create the Topping Decorator clas
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.pizza = pizza
    
    # Creating an abstract method for description
    @abstractmethod
    def get_description(self):
        pass

    # Creating an abstract method for cost
    def get_cost(self):
        pass

# Now let's create the concrete classes of the Topping CLass
class Olives(ToppingDecorator):
    # Here we need to modify the description
    def get_description(self):
        return self.pizza.get_description() + ", Olives"
    
    # Also update the cost
    def get_cost(self):
        return self.pizza.get_cost() + 1
    
class Chicken(ToppingDecorator):
    # Here we need to modify the description
    def get_description(self):
        return self.pizza.get_description() + ", Chicken"
    
    # Also update the cost
    def get_cost(self):
        return self.pizza.get_cost() + 2
    
class Corn(ToppingDecorator):
    # Here we need to modify the description
    def get_description(self):
        return self.pizza.get_description() + ", Corn"
    
    # Also update the cost
    def get_cost(self):
        return self.pizza.get_cost() + 0.5
    

# Creating the main function to instantiate the Pizza class
if __name__ == "__main__":

    # Creating the Margherita Pizza
    pizza_1 = Margherita()
    # Adding Toppings to the pizza
    pizza_1 = Olives(pizza_1)
    pizza_1 = Corn(pizza_1)
    pizza_1 = Olives(pizza_1)

    print(f"Pizza Description : {pizza_1.get_description()}, and Cost : {pizza_1.get_cost()}")