
# Creating the class for Ingredients
class Ingredients:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    # Creating the get name method
    def get_name(self):
        return self.name

    # Creating the method of get_quantity
    def get_quantity(self):
        return self.quantity
    
    # Creating the method of update_quantity
    def update_quantity(self, amount):
        self.quantity += amount

# Creating the class for Coffee
class Coffee:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe
    
    # Creating the method of get_name
    def get_name(self):
        return self.name

    # Creating the method of get_price
    def get_price(self):
        return self.price
    
    # Creatting the method of get_recipe
    def get_recipe(self):
        return self.recipe
    
# Creating the class for Payment
class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    # Craeting the method of get_amount
    def get_amount(self):
        return self.amount

# Creating the class for CoffeeMachine
class CoffeeMachine:
    _instance = None

    def __init__(self):
        if CoffeeMachine._instance is not None:
            raise Exception("This class is a singleton !")
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
    
    # Creating the method of  initializing the Coffee Menu
    def _initialize_coffee_menu(self):
        # Espresso, Cappauchino, Latte
        espresso_recipie = {
            self.ingredients['Coffee'] : 1,
            self.ingredients['Water'] : 1
        }

        self.coffee_menu.append(Coffee("Espresso", 2, espresso_recipie))

        cappauchino_recipie = {
            self.ingredients['Coffee'] : 2,
            self.ingredients['Water'] : 1,
            self.ingredients['Milk'] : 1
        }

        self.coffee_menu.append(Coffee("Cappauchino", 4, cappauchino_recipie))

        latte_recipie = {
            self.ingredients['Coffee'] : 2,
            self.ingredients['Milk'] : 2
        }

        self.coffee_menu.append(Coffee("Latte", 3.5, latte_recipie))
    
    # Creating the method of initializing the ingredients, this checks if the ingredients are already present or not
    def _initialize_ingredients(self):
        self.ingredients["Coffee"] = Ingredients("Coffee", 10)
        self.ingredients["Water"] = Ingredients("Water", 10)
        self.ingredients["Milk"] = Ingredients("Milk", 10)
    
    # Creating the method for displaying the menu
    def display_menu(self):
        print("\nCoffee Menu:")
        for items in self.coffee_menu:
            print(f"\n{items.get_name()} - ${items.get_price()}")
    
    # Creating the method for selecting the coffee
    def select_coffee(self, coffee_name):
        for coffee in self.coffee_menu:
            if coffee.get_name() == coffee_name:
                return coffee
        return None
    
    # Creating the method fo making the coffee
    def dispense_coffee(self, coffee, payment):
        if not coffee:
            print("Coffee not available")
            return
        
        if payment.get_amount() >= coffee.get_price():
            if self._has_ingredients(coffee):
                self.update_ingredients(coffee)
                print(f"\n Dispensing the {coffee.get_name()}...")
                change = payment.get_amount() - coffee.get_price()
                if change > 0:
                    print(f"Please collect you change : ${change:.2f}")
                    print("Payment successfull !!!... Enjoy your Coffee")
                else:
                    print("Payment successfull !!!... Enjoy your Coffee")
            else:
                print(f"Insufficient Ingredients to make the {coffee.get_name()}")
        else:
            print(f"Insufficient Payment for the {coffee.get_name()}")

    def _has_ingredients(self, coffee):
        for ingredients, required_quantity in coffee.get_recipe().items():
            if ingredients.get_quantity() < required_quantity:
                return False
        return True        

    def update_ingredients(self, coffee):
        for ingredients, required_quantity in coffee.get_recipe().items():
            ingredients.update_quantity(-required_quantity)
            if ingredients.get_quantity() < 3:
                print(f"Warning: {ingredients.get_name()} is running low !")
            print(f"Remaining Quantity of {ingredients.get_name()} is {ingredients.get_quantity()}")

# Creating the Main Method
if __name__ == "__main__":

    # Get the instance of the Coffee Machine
    coffee_machine = CoffeeMachine.get_instance()

    # Display the Menu
    coffee_machine.display_menu()

    # Coffee Selection
    user_1 = coffee_machine.select_coffee("Espresso")
    coffee_machine.dispense_coffee(user_1, Payment(2))

    user_2 = coffee_machine.select_coffee("Cappauchino")
    coffee_machine.dispense_coffee(user_2, Payment(4.5))
    
    user_3 = coffee_machine.select_coffee("Latte")
    coffee_machine.dispense_coffee(user_3, Payment(1))

