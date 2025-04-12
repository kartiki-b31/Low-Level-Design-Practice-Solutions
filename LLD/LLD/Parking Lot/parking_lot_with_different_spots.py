from threading import Lock
from enum import Enum
from abc import ABC, abstractmethod

# Enum for Vehicle Types
class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3

# Abstract Vehicle Class
class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    @abstractmethod
    def get_vehicle_type(self):
        pass

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.CAR)

    def get_vehicle_type(self):
        return self.vehicle_type

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

    def get_vehicle_type(self):
        return self.vehicle_type

class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.TRUCK)

    def get_vehicle_type(self):
        return self.vehicle_type

# Parking Spot Class
class ParkingSpot:
    def __init__(self, spot_id, vehicle_type):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.occupied = False
        self.vehicle = None
        self.lock = Lock()

    def park_vehicle(self, vehicle):
        with self.lock:
            if not self.occupied and vehicle.get_vehicle_type() == self.vehicle_type:
                self.vehicle = vehicle
                self.occupied = True
                return True
            return False

    def remove_vehicle(self):
        with self.lock:
            if self.occupied:
                vehicle = self.vehicle
                self.vehicle = None
                self.occupied = False
                return vehicle
            return None

    def is_available(self):
        return not self.occupied

# Level Class
class Level:
    def __init__(self, level_id, num_spots):
        self.level_id = level_id
        self.spots = []
        self.lock = Lock()

        # Creating spots (equal distribution for each type)
        for i in range(num_spots // 3):
            self.spots.append(ParkingSpot(f"{level_id}-M-{i}", VehicleType.MOTORCYCLE))
        for i in range(num_spots // 3, 2 * num_spots // 3):
            self.spots.append(ParkingSpot(f"{level_id}-C-{i}", VehicleType.CAR))
        for i in range(2 * num_spots // 3, num_spots):
            self.spots.append(ParkingSpot(f"{level_id}-T-{i}", VehicleType.TRUCK))

    def park_vehicle(self, vehicle):
        with self.lock:
            for spot in self.spots:
                if spot.is_available() and spot.vehicle_type == vehicle.get_vehicle_type():
                    if spot.park_vehicle(vehicle):
                        print(f"✅ Vehicle {vehicle.license_plate} parked at spot {spot.spot_id}")
                        return True
        return False

    def remove_vehicle(self, license_plate):
        with self.lock:
            for spot in self.spots:
                if spot.occupied and spot.vehicle.license_plate == license_plate:
                    removed_vehicle = spot.remove_vehicle()
                    print(f"❌ Vehicle {license_plate} left spot {spot.spot_id}")
                    return removed_vehicle
        return None

    def display_level(self):
        print(f"\n📍 **Level {self.level_id} Status:**")
        for spot in self.spots:
            if spot.occupied:
                print(f"🟢 {spot.spot_id} → {spot.vehicle.license_plate}")
            else:
                print(f"🔴 {spot.spot_id} → [Empty]")

# Parking Lot (Singleton)
class ParkingLot:
    _instance = None
    _lock = Lock()

    def __new__(cls, num_levels=1, spots_per_level=10):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ParkingLot, cls).__new__(cls)
                cls._instance.num_levels = num_levels
                cls._instance.levels = [Level(i, spots_per_level) for i in range(num_levels)]
        return cls._instance

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                self.display_board()  # Display updated parking status
                return True
        print(f"🚫 No parking spots available for {vehicle.license_plate}")
        return False

    def remove_vehicle(self, license_plate):
        for level in self.levels:
            removed_vehicle = level.remove_vehicle(license_plate)
            if removed_vehicle:
                self.display_board()  # Display updated parking status
                return True
        print(f"⚠️ Vehicle {license_plate} not found in the parking lot")
        return False

    def display_board(self):
        print("\n📢 **Parking Lot Status:**")
        for level in self.levels:
            level.display_level()
        print("\n")

# Demonstration of the Parking Lot System
if __name__ == "__main__":
    # Create a Parking Lot with 2 Levels, Each Level having 6 Spots
    parking_lot = ParkingLot(num_levels=2, spots_per_level=6)
    parking_lot = ParkingLot(num_levels=2, spots_per_level=6)
    # Create Vehicles
    car1 = Car("ABC123")
    car2 = Car("XYZ789")
    car3 = Car("New_CAR")
    bike1 = Motorcycle("MOTO999")
    truck1 = Truck("TRUCK555")

    # Park Vehicles
    parking_lot.park_vehicle(car1)
    parking_lot.park_vehicle(car2)
    parking_lot.park_vehicle(car3)
    parking_lot.park_vehicle(bike1)
    parking_lot.park_vehicle(truck1)

    # Remove Vehicles
    parking_lot.remove_vehicle("ABC123")
    parking_lot.remove_vehicle("MOTO999")

    # Attempt to park again
    parking_lot.park_vehicle(Car("NEW456"))



