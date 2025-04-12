# Does the parking have multiple floors ? No
# Any particular number of parking spots  - 10
# # Types of vehicles to park ? - Car, Bike 
# Do we have any differnet types of parking spot? No

from enum import Enum
from typing import List
from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2

# Creating the Abstract class of Vehicle
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicletype : VehicleType):
        self.license_plate = license_plate
        self.type = vehicletype
    
    def get_type(self)-> VehicleType:
        return self.type
    
# Creating the concrete classes for Vehicle
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

class MotorCycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)
    

# Creating the class for Parking Spot
class ParkingSpot:
    def __init__(self, spot_num: int):
        self.spot_num = spot_num
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available():
            self.parked_vehicle = vehicle
        else:
            raise ValueError(f"Spot {self.spot_num} is already occupied.")
    
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
    
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

# Creating the Class for Parking Lot
class ParkingLot:
    _instance = None

    def __init__(self, num_spots: int):
        if ParkingLot._instance is not None:
            raise Exception("This is a Singleton Class")
        else:
            ParkingLot._instance = self 
            # Since there is only one floor with multpile spots
            self.spots = [ParkingSpot(i) for i in range(num_spots)]

    # Creating the function for Park Vehicle
    def park_vehicle(self, vehicle: Vehicle, spot: int) -> bool:
        if 0<= spot < len(self.spots):
            if self.spots[spot].is_available():
                self.spots[spot].park_vehicle(vehicle)
                print(f"Vehicle with the number {vehicle.license_plate} is parked at spot {spot}")
                # displaying available spots
                self.display_available_spots()
                return True
            else:
                print(f"Spot {spot} is already occupied")
                return False
        else:
            print(f"Invalid Spot Number")
            return False
    
    # Creating the function for unpark_vehicle:
    def unpark_vehicle(self, spot: int) -> bool:
        if 0 <= spot < len(self.spots):
            if not self.spots[spot].is_available():
                vehicle = self.spots[spot].get_parked_vehicle()
                self.spots[spot].unpark_vehicle()
                print(f"Vehicle {vehicle.license_plate} removed from spot {spot}")
                # displaying available spots
                self.display_available_spots()
                return True
            else:
                print(f"No Vehicle is parked at spot {spot}")
                return False
        else:
            print(f"Invalid Spot Number")
            return False
    
    # displaying the avaiable spots
    def display_available_spots(self) -> None:
        for spot in self.spots:
            if spot.is_available():
                print(f"spot {spot.spot_num} is available")


# Creating the main function
if __name__ == "__main__":

    # creating a parking lot with predefined spots
    parkinglot = ParkingLot(10)

    # Creating the car objects
    car_1 = Car("CAR-1-001")
    car_2 = Car("CAR-2-002")
    car_3 = Car("CAR-3-003")

    # Creating objects for the Motorcycle
    bike_1 = MotorCycle("BIKE-1-001")
    bike_2 = MotorCycle("BIKE-2-002")

    # Parking the Car and Bike
    parkinglot.park_vehicle(car_1, 1)

    parkinglot.park_vehicle(car_2, 2)

    # Intentionally parking the car 3 at spot 1
    parkinglot.park_vehicle(car_3, 1) # this should raise an error

    # Unparking the car 1
    parkinglot.unpark_vehicle(1)
    # Trying again to park the car 3 at spot 1
    parkinglot.park_vehicle(car_3, 1)

    # Parking the Bike
    parkinglot.park_vehicle(bike_1, 3)
    parkinglot.unpark_vehicle(3)
    parkinglot.park_vehicle(bike_2, 3) 

