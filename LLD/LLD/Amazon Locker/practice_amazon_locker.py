from enum import Enum
import random

# Package Size class
class PackageSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Creating the class for Locker
class Locker:
    def __init__(self, locker_id : int, size: PackageSize):
        pass
    
    # Creating a assign method
    def assign(self, customer, pin : int):
        pass

    # Creating a free method
    def free(self):
        pass

    # Creating the Check_pin function
    def check_pin(self, pin : int):
        pass

# Creating the class for Customer
class Customer:
    def __init__(self, customer_id: int):
        pass

    # Creating the update method
    def update(self, locker_id: int, pin: int):
        pass

    # Creating the remove_locker method
    def remove_locker(self, locker_id: int):
        pass

    # Creating the order_package method
    def order_package(self, package_size: PackageSize, amazon_locker_system, locker_id: int):
        pass

    # Creating the unassign_locker method
    def unassign_locker(self, locker_id:int, pin: int):
        pass

# Creating hte Amazon Locker System Class
class AmazonLockerSystem:
    # Creating a new instance of the class
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__cls(cls)
            cls._instance.locker_location = None
        return cls._instance

    # Creating a set_location method
    def set_location(self, location):
        pass

    # Creating the assign_locker:
    def assign_locker(self, customer, package_size: PackageSize, locker_id: int):
        pass

    # Creating the unlock_locker method
    def unlock_locker(self, cusomter, locker_id : int, pin : int):
        pass

# Creating the Location class
class Location:
    def __init__(self):
        self.locker = {
            PackageSize.SMALL : [Locker(i, PackageSize.SMALL) for i in range(1, 21)],
            PackageSize.MEDIUM : [Locker(i, PackageSize.MEDIUM) for i in range(1, 41)],
            PackageSize.LARGE : [Locker(i, PackageSize.LARGE) for i in range(1, 61)]
        }


# Creating the main function
if __name__ == "__main__":

    # Creating the Amazon Locker System
    als = AmazonLockerSystem()
    location = Location()
    als.set_location(location)

    # Creating the customers
    c1 = Customer(1)
    c2 = Customer(2)

    # Ordering the packages
    c1.order_package(PackageSize.Large, als, 41)
    c1.unassign_locker(41, c1.assigned_locker[41])


