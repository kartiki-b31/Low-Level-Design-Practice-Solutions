


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
            raise ValueError(f"🚫 Spot {self.spot_number} is already occupied.")

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

    def display_availability(self) -> None:
        """Displays the available and occupied spots on this level."""
        print(f"\n📍 **Level {self.floor - 1} Availability:**")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()}: {'🟢 Available' if spot.is_available() else '🔴 Occupied'}")
        print("\n")

    def park_vehicle(self, vehicle: Vehicle, spot_number: int) -> bool:
        """Parks the vehicle at the specified spot if available."""
        if 0 <= spot_number < len(self.parking_spots):
            selected_spot = self.parking_spots[spot_number]

            if selected_spot.is_available():
                selected_spot.park_vehicle(vehicle)
                print(f"✅ Vehicle {vehicle.license_plate} parked at spot {spot_number} on Level {self.floor - 1}")
                self.display_availability()
                return True
            else:
                print("🚫 Selected spot is already occupied. Choose another spot.")
        else:
            print("⚠️ Invalid spot number. Please select a valid parking spot.")
        return False

    def unpark_vehicle(self, spot_number: int) -> bool:
        """Unparks a vehicle from the specified spot."""
        if 0 <= spot_number < len(self.parking_spots):
            selected_spot = self.parking_spots[spot_number]

            if not selected_spot.is_available():
                vehicle = selected_spot.get_parked_vehicle()
                selected_spot.unpark_vehicle()
                print(f"❌ Vehicle {vehicle.license_plate} removed from spot {spot_number} on Level {self.floor - 1}")
                self.display_availability()
                return True
            else:
                print("🚫 No vehicle is parked in this spot. Choose another.")
        else:
            print("⚠️ Invalid spot number. Please enter a valid spot.")
        return False

# Parking Lot Singleton Class
class ParkingLot:
    _instance = None

    def __init__(self):
        """Ensures only one instance of ParkingLot exists (Singleton pattern)."""
        if ParkingLot._instance is not None:
            raise Exception("🚫 This class is a singleton!")
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

    def park_vehicle(self, vehicle: Vehicle, level: int, slot: int) -> bool:
        """Attempts to park a vehicle at the specified level and slot."""
        if 0 <= level < len(self.levels):
            return self.levels[level].park_vehicle(vehicle, slot)
        else:
            print("⚠️ Invalid level selection.")
            return False

    def unpark_vehicle(self, level: int, slot: int) -> bool:
        """Removes a vehicle from the specified parking level and slot."""
        if 0 <= level < len(self.levels):
            return self.levels[level].unpark_vehicle(slot)
        else:
            print("⚠️ Invalid level selection.")
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

    # Park Vehicles (Manual Slot & Level Selection)
    parking_lot.park_vehicle(car1, level=0, slot=1)
    parking_lot.park_vehicle(car2, level=1, slot=2)
    parking_lot.park_vehicle(bike1, level=0, slot=0)
    parking_lot.park_vehicle(truck1, level=1, slot=4)

    # Remove Vehicles (Manual Slot & Level Selection)
    parking_lot.unpark_vehicle(level=0, slot=1)
    parking_lot.unpark_vehicle(level=1, slot=2)

    # Attempt to park again
    parking_lot.park_vehicle(new_car, level=0, slot=3)
