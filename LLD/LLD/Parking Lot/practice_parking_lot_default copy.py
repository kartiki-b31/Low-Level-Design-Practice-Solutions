# Diff Floors : No
# Diff spots : No
# Vehicle Types : Car, Truck, Bike
# Default Parking Spots number : 10
# Display available spots : Yes

from enum import Enum
from abc import ABC, abstractmethod

# Creating the Class for VEhicle Type
class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

# Creating the Abstract class for Vehicle
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
    
    # Creating the method for getting the type of vehicle
    def get_type(self):
        return self.vehicle_type

# Creating the concrete classes for Vehicle
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.BIKE)
    
class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)
    
# Creating the class for Parking Spot
class ParkingSpot:
    def __init__(self, spot_num: int):
        self.spot_num = spot_num
        self.parked_vehicle = None
    
    # Creating the method for checking the availability of the spot
    def is_available(self):
        return self.parked_vehicle is None
    
    # Creating the method to park the vehicle
    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available():
            self.parked_vehicle = vehicle
        else:
            raise ValueError(f"Spot {self.spot_num} is already occupied.")
    
    # Creating the method to unpark the vehicle
    def unpark_vehicle(self):
        self.parked_vehicle = None
    
    # Creating the method to get the parked vehicle
    def get_parked_vehicle(self):
        return self.parked_vehicle

# Creating the class for Parking Lot
class ParkingLot:
    _instance = None
    
    def __init__(self, spots: int):
        if ParkingLot._instance is not None:
            raise Exception("This is a Singleton Class, should not be instantiated multiple times.")
        else:
            ParkingLot._instance = self
            self.spots = [ParkingSpot(i) for i in range(spots)]
    
    # Creating the method to park the vehicle
    def park_vehicle(self, vehicle: Vehicle, spot: int):
        if 0<= spot < len(self.spots):
            if self.spots[spot].is_available():
                self.spots[spot].park_vehicle(vehicle)
                print(f"Vehicle with the number {vehicle.license_plate} is parkedd at the spot {spot}")
                self.display_availability()
                return True
            else:
                print(f"The spot {spot} is already occupied")
                return False
        else:
            print(f"Invalid Spot Number {spot}")
            return False
        
    # Creating the method to unpark the vehicle
    def unpark_vehicle(self, spot: int):
        if 0 <= spot < len(self.spots):
            if not self.spots[spot].is_available():
                vehicle = self.spots[spot].get_parked_vehicle()
                self.spots[spot].unpark_vehicle()
                print(f"Vehicle {vehicle.license_plate} removed from spot {spot}")
                return True
            else:
                print(f"No vehilce found at spot {spot}")
                return False
        else:
            print(f"Invalid Spot Number {spot}")
            return False
    
    # Creating the method to display the available spot
    def display_availability(self):
        for spot in self.spots:
            print(f"spot {spot.spot_num}: {"🟢 Available" if spot.is_available() else "🔴 Occupied"}")

# Creating the Main function
if __name__ == "__main__":

    # Creating the Parking Lot with 10 spots
    parking_lot = ParkingLot(10)

    # Creating Cars, Bikes and Trucks
    car1 = Car("Car1 - 001")
    car2 = Car("Car2 - 002")
    bike1 = Bike("Bike1 - 001")
    truck1 = Truck("Truck - 001")

    # Parking the vehicles
    parking_lot.park_vehicle(car1, 0)
    parking_lot.park_vehicle(car2, 1)
    parking_lot.park_vehicle(bike1, 1)
    parking_lot.park_vehicle(truck1, 3)
    
    # unpark car2 from spot 1
    parking_lot.unpark_vehicle(1)
    parking_lot.park_vehicle(bike1, 1)
