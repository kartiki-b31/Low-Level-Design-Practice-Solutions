from enum import Enum
from typing import List

# Enum for Vehicle Types
class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3

from abc import ABC

# Abstract base class for all vehicles
class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.type = vehicle_type

    def get_type(self) -> VehicleType:
        return self.type

# Subclasses for different vehicle types
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)

# Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.parked_vehicle = None  # Stores the vehicle currently occupying this spot

    def is_available(self) -> bool:
        """Returns True if the parking spot is available."""
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle) -> None:
        """Parks a vehicle in the spot if available."""
        if self.is_available():
            self.parked_vehicle = vehicle
        else:
            raise ValueError(f"Spot {self.spot_number} is already occupied.")

    def unpark_vehicle(self) -> None:
        """Removes the vehicle from the spot."""
        self.parked_vehicle = None

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def get_spot_number(self) -> int:
        return self.spot_number

# Parking Level Class
class Level:
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """Finds the next available spot and parks the vehicle."""
        for spot in self.parking_spots:
            if spot.is_available():
                spot.park_vehicle(vehicle)
                print(f"✅ Vehicle {vehicle.license_plate} parked at spot {spot.get_spot_number()} on Level {self.floor}")
                self.display_availability()
                return True
        print(f"🚫 No parking spots available for {vehicle.license_plate}")
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        """Finds the vehicle and removes it from the parking spot."""
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                print(f"❌ Vehicle {vehicle.license_plate} left spot {spot.get_spot_number()} on Level {self.floor}")
                self.display_availability()
                return True
        print(f"⚠️ Vehicle {vehicle.license_plate} not found in the parking lot")
        return False

    def display_availability(self) -> None:
        """Displays the available and occupied spots on this level."""
        print(f"\n📍 **Level {self.floor} Availability:**")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()}: {'🟢 Available' if spot.is_available() else '🔴 Occupied'}")
        print("\n")

# Parking Lot Singleton Class
class ParkingLot:
    _instance = None

    def __init__(self):
        """Ensures only one instance of ParkingLot exists (Singleton pattern)."""
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []

    @staticmethod
    def get_instance():
        """Returns the single instance of the ParkingLot."""
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self, level: Level) -> None:
        """Adds a new parking level to the parking lot."""
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """Attempts to park a vehicle in the next available spot."""
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        print(f"🚫 No parking spots available for {vehicle.license_plate}")
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        """Attempts to remove a vehicle from the parking lot."""
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        print(f"⚠️ Vehicle {vehicle.license_plate} not found in the parking lot")
        return False

    def display_availability(self) -> None:
        """Displays the overall parking lot availability."""
        for level in self.levels:
            level.display_availability()

# --------------------- DEMONSTRATION ---------------------
if __name__ == "__main__":
    # Create a Parking Lot (Singleton) and add levels
    parking_lot = ParkingLot.get_instance()
   
    parking_lot.add_level(Level(1, 5))  # Level 1 with 5 spots
    parking_lot.add_level(Level(2, 5))  # Level 2 with 5 spots

    # Create Vehicles
    car1 = Car("ABC123")
    car2 = Car("XYZ789")
    bike1 = Motorcycle("MOTO999")
    truck1 = Truck("TRUCK555")
    new_car = Car("NEW456")

    # Park Vehicles
    parking_lot.park_vehicle(car1)
    parking_lot.park_vehicle(car2)
    parking_lot.park_vehicle(bike1)
    parking_lot.park_vehicle(truck1)
    parking_lot.park_vehicle(truck1)
    parking_lot.park_vehicle(truck1)
    # Remove Vehicles
    parking_lot.unpark_vehicle(car1)
    parking_lot.unpark_vehicle(bike1)

    # Attempt to park again
    parking_lot.park_vehicle(new_car)

