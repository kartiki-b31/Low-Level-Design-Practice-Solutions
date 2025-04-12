from enum import Enum
import random

# Enum for package sizes
class PackageSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Locker class representing individual lockers
class Locker:
    def __init__(self, locker_id: int, size: PackageSize):
        self.locker_id = locker_id
        self.size = size
        self.is_assigned = False
        self.pin = None
        self.assigned_customer = None  # Track current assigned customer

    def assign(self, customer, pin: int):
        """ Assign locker to a customer with a PIN and notify them """
        self.is_assigned = True
        self.pin = pin
        self.assigned_customer = customer
        customer.update(self.locker_id, self.pin)  # Notify the customer

    def free(self):
        """ Free up the locker and remove customer association """
        if self.assigned_customer:
            self.assigned_customer.remove_locker(self.locker_id)  # Remove from customer's record
        self.is_assigned = False
        self.pin = None
        self.assigned_customer = None  # Remove assigned customer reference

    def check_pin(self, pin: int) -> bool:
        """ Validate PIN before allowing access """
        return self.is_assigned and self.pin == pin

# Customer class representing a customer
class Customer:
    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        self.assigned_lockers = {}  # Stores multiple locker assignments {locker_id: pin}

    def update(self, locker_id: int, pin: int):
        """ Receive notification when locker is assigned """
        self.assigned_lockers[locker_id] = pin
        print(f"🔔 Notification: Customer {self.customer_id} - Assigned Locker {locker_id}, PIN: {pin}")

    def remove_locker(self, locker_id: int):
        """ Remove locker from the customer's assigned list """
        if locker_id in self.assigned_lockers:
            del self.assigned_lockers[locker_id]

    def order_package(self, package_size: PackageSize, amazon_locker_system, locker_id: int):
        """ Place an order and request a specific locker """
        amazon_locker_system.assign_locker(self, package_size, locker_id)

    def unassign_locker(self, locker_id: int, pin: int):
        """ Attempt to unlock a specific locker with Locker ID & PIN """
        if locker_id in self.assigned_lockers and self.assigned_lockers[locker_id] == pin:
            amazon_locker_system.unlock_locker(self, locker_id, pin)
        else:
            print(f"❌ Customer {self.customer_id}: Invalid Locker ID or Incorrect PIN.")

# Amazon Locker Management System (Singleton)
class AmazonLockerSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.locker_location = None
        return cls._instance

    def set_location(self, location):
        """ Set the single location containing lockers """
        self.locker_location = location

    def assign_locker(self, customer, package_size: PackageSize, locker_id: int):
        """ Manually assign a specific locker chosen by the courier """
        if not self.locker_location:
            print("❌ Locker location not set.")
            return False

        # Determine locker size based on its ID
        if 1 <= locker_id <= 20:
            locker_list = self.locker_location.lockers[PackageSize.SMALL]
        elif 21 <= locker_id <= 40:
            locker_list = self.locker_location.lockers[PackageSize.MEDIUM]
        elif 41 <= locker_id <= 60:
            locker_list = self.locker_location.lockers[PackageSize.LARGE]
        else:
            print(f"❌ Locker {locker_id} not found.")
            return False

        # Get the specific locker (adjusting index)
        locker = locker_list[(locker_id - 1) % 20]

        if locker.is_assigned:
            print(f"❌ Locker {locker_id} is already assigned. Choose another locker.")
            return False

        # Validate size compatibility
        if package_size == PackageSize.LARGE and locker.size == PackageSize.SMALL:
            print(f"❌ Cannot place a LARGE package in a SMALL locker! Choose a bigger locker.")
            return False

        if package_size == PackageSize.LARGE and locker.size == PackageSize.MEDIUM:
            print(f"❌ Cannot place a LARGE package in a SMALL locker! Choose a bigger locker.")
            return False

        if package_size == PackageSize.MEDIUM and locker.size == PackageSize.SMALL:
            print(f"❌ Cannot place a LARGE package in a SMALL locker! Choose a bigger locker.")
            return False

        # Assign the locker with a random PIN
        pin = random.randint(1000, 9999)
        locker.assign(customer, pin)
        print(f"✅ Locker {locker_id} assigned to Customer {customer.customer_id} for package size {package_size.name}.")
        return True


    def unlock_locker(self, customer, locker_id: int, pin: int):
        """ Allow the customer to unlock a specific locker with the correct PIN """
        if not self.locker_location:
            print("❌ Locker location not set.")
            return False

        # Determine the correct locker list based on locker ID
        if 1 <= locker_id <= 20:
            locker_list = self.locker_location.lockers[PackageSize.SMALL]
        elif 21 <= locker_id <= 40:
            locker_list = self.locker_location.lockers[PackageSize.MEDIUM]
        elif 41 <= locker_id <= 60:
            locker_list = self.locker_location.lockers[PackageSize.LARGE]
        else:
            print(f"❌ Locker {locker_id} not found.")
            return False

        # Get the specific locker (adjusting index)
        locker = locker_list[(locker_id - 1) % 20]

        # Check if locker is assigned and verify PIN
        if locker.is_assigned:
            if locker.check_pin(pin):
                print(f"🔓 Customer {customer.customer_id}: Locker {locker_id} Unlocked Successfully! Package Retrieved.")
                locker.free()  # Free the locker after successful retrieval
                return True
            else:
                print(f"❌ Customer {customer.customer_id}: Wrong PIN for Locker {locker_id}. Access Denied.")
                return False

        print(f"❌ Locker {locker_id} is not assigned or does not exist.")
        return False

# Location class representing a single location with lockers
class Location:
    def __init__(self):
        """ Initialize the locker system with 60 lockers (20 small, 20 medium, 20 large) """
        self.lockers = {
            PackageSize.SMALL: [Locker(i, PackageSize.SMALL) for i in range(1, 21)],
            PackageSize.MEDIUM: [Locker(i, PackageSize.MEDIUM) for i in range(21, 41)],
            PackageSize.LARGE: [Locker(i, PackageSize.LARGE) for i in range(41, 61)],
        }

# Example usage
if __name__ == "__main__":
    # Create Amazon Locker System (Singleton)
    amazon_locker_system = AmazonLockerSystem()

    # Create a single location and set it in the system
    location = Location()
    amazon_locker_system.set_location(location)

    # Create customers
    customer1 = Customer(1)
    customer2 = Customer(2)
    customer3 = Customer(3)

    # Customers place orders manually by specifying locker ID
    customer1.order_package(PackageSize.SMALL, amazon_locker_system, 5)   # ✅ Assigns locker 5
    customer2.order_package(PackageSize.MEDIUM, amazon_locker_system, 25) # ✅ Assigns locker 25
    customer3.order_package(PackageSize.LARGE, amazon_locker_system, 45)  # ✅ Assigns locker 45

    # Edge Cases:
    customer1.order_package(PackageSize.LARGE, amazon_locker_system, 10)  # ❌ Large package in small locker
    customer2.order_package(PackageSize.SMALL, amazon_locker_system, 25)  # ❌ Already assigned locker
    customer3.order_package(PackageSize.MEDIUM, amazon_locker_system, 70) # ❌ Invalid locker ID

    # Customers retrieve their packages
    customer1.unassign_locker(5, customer1.assigned_lockers[5])   # ✅ Should succeed
    customer2.unassign_locker(25, customer2.assigned_lockers[25]) # ✅ Should succeed
    customer3.unassign_locker(45, customer3.assigned_lockers[45]) # ✅ Should succeed
    customer3.order_package(PackageSize.LARGE, amazon_locker_system, 45)