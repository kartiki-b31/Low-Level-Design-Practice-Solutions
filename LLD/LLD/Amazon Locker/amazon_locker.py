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

    def order_package(self, package_size: PackageSize, amazon_locker_system):
        """ Place an order and request a locker """
        amazon_locker_system.assign_locker(self, package_size)

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

    def find_available_locker(self, package_size: PackageSize):
        """ Find an available locker based on nesting rules """
        if not self.locker_location:
            return None

        if package_size == PackageSize.SMALL:
            # Try small lockers first, then fallback to medium, then large
            for size in [PackageSize.SMALL, PackageSize.MEDIUM, PackageSize.LARGE]:
                for locker in self.locker_location.lockers[size]:
                    if not locker.is_assigned:
                        return locker

        elif package_size == PackageSize.MEDIUM:
            # Try medium lockers first, then fallback to large
            for size in [PackageSize.MEDIUM, PackageSize.LARGE]:
                for locker in self.locker_location.lockers[size]:
                    if not locker.is_assigned:
                        return locker

        elif package_size == PackageSize.LARGE:
            # Large packages can only go into large lockers
            for locker in self.locker_location.lockers[PackageSize.LARGE]:
                if not locker.is_assigned:
                    return locker

        return None  # No available locker found

    def assign_locker(self, customer, package_size: PackageSize):
        """ Assign an available locker based on package size constraints """
        locker = self.find_available_locker(package_size)
        if locker:
            pin = random.randint(1000, 9999)
            locker.assign(customer, pin)
            return True
        else:
            print(f"❌ No available lockers for Customer {customer.customer_id}. Please try later.")
            return False

    def unlock_locker(self, customer, locker_id: int, pin: int):
        """ Allow the customer to unlock a specific locker with the correct PIN """
        for size in self.locker_location.lockers:
            for locker in self.locker_location.lockers[size]:
                if locker.locker_id == locker_id and locker.is_assigned:
                    if locker.check_pin(pin):
                        print(f"🔓 Customer {customer.customer_id}: Locker {locker_id} Unlocked Successfully! Package Retrieved.")
                        locker.free()  # Properly free locker before reassigning
                        return
                    else:
                        print(f"❌ Customer {customer.customer_id}: Wrong PIN for Locker {locker_id}. Access Denied.")
                        return
        print(f"❌ Customer {customer.customer_id}: Invalid Locker ID or Locker Not Assigned.")

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

    # Customers place orders
    customer1.order_package(PackageSize.SMALL, amazon_locker_system)
    customer1.order_package(PackageSize.SMALL, amazon_locker_system)  # Assign another locker
    customer2.order_package(PackageSize.MEDIUM, amazon_locker_system)

    customer1.unassign_locker(1, customer1.assigned_lockers[1])  # Should succeed

    customer3.order_package(PackageSize.SMALL, amazon_locker_system)
    customer3.order_package(PackageSize.SMALL, amazon_locker_system)
    customer3.order_package(PackageSize.SMALL, amazon_locker_system)
    customer3.order_package(PackageSize.SMALL, amazon_locker_system)
    customer3.order_package(PackageSize.SMALL, amazon_locker_system)

    customer3.unassign_locker(2, customer1.assigned_lockers[2])  # Should succeed

    customer1.unassign_locker(2, customer1.assigned_lockers[2])  # Should succeed

    customer3.unassign_locker(4, customer3.assigned_lockers[4]) 
    customer3.order_package(PackageSize.SMALL, amazon_locker_system)