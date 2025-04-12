### **VehicleType (Enum)**

This is an **enumeration (Enum)** that defines different vehicle types:

- **CAR**
- **MOTORCYCLE**

Enums are used here because vehicle types are fixed, and each type is assigned a unique integer value. Using an Enum ensures **type safety** and makes comparisons more efficient.

---

### **Vehicle (Abstract Base Class)**

The `Vehicle` class serves as a **base class** for all vehicles (Car, Motorcycle).

- It is **abstract** because we don't want to instantiate `Vehicle` directly. Instead, specific vehicle types like `Car` and `MotorCycle` will inherit from it.
- The constructor initializes the **license plate** and **vehicle type**.
- The function `get_type()` returns the **type of vehicle** (CAR or MOTORCYCLE).
- By making `Vehicle` an **abstract class**, we ensure that every vehicle type must define its own behavior while maintaining a common structure.

---

### **Car & MotorCycle (Concrete Classes)**

These classes **inherit from the `Vehicle` class** and define specific vehicle types:

- `Car` initializes itself with the vehicle type **CAR**.
- `MotorCycle` initializes itself with the vehicle type **MOTORCYCLE**.
- Since they inherit from `Vehicle`, they automatically have the **license plate** and **get_type()** function.

Each vehicle instance will carry a **unique license plate number** to identify it.

---

### **ParkingSpot (Class)**

A **ParkingSpot** represents an individual parking space in the lot.  
Each spot has:

- `spot_num` – A unique identifier for the spot.
- `parked_vehicle` – Stores the **vehicle currently occupying** the spot (or None if the spot is empty).

#### **Functions in ParkingSpot**

1. **`is_available()`** – Checks if the spot is empty by verifying if `parked_vehicle` is `None`.
2. **`park_vehicle(vehicle)`** – Assigns a vehicle to the spot **if it is available**.
    - If the spot is already occupied, an **exception is raised**.
3. **`unpark_vehicle()`** – Removes the vehicle from the spot.
4. **`get_parked_vehicle()`** – Returns the vehicle that is currently parked in this spot.

This class ensures **spot-level management**, allowing us to track vehicle assignments efficiently.

---

### **ParkingLot (Singleton Class)**

The **ParkingLot** class represents the **entire parking area** and follows the **Singleton Design Pattern**:

- The singleton ensures **only one instance** of the parking lot exists.
- If someone tries to create a second instance, an **exception is raised**.

#### **Attributes**

- `spots` – A list of `ParkingSpot` objects representing the available parking spaces.

#### **Functions in ParkingLot**

1. **`park_vehicle(vehicle, spot)`**
    
    - This function takes a **vehicle** and a **spot number**.
    - First, it checks if the spot is within the valid range (between 0 and the total number of spots).
    - If the spot is **available**, it parks the vehicle and displays the updated availability.
    - If the spot is **already occupied**, it prints an error message.
2. **`unpark_vehicle(spot)`**
    
    - This function attempts to **remove a vehicle** from the given spot.
    - If the spot is empty, an error message is displayed.
    - If a vehicle is found, it is removed, and the availability is updated.
3. **`display_available_spots()`**
    
    - This function loops through all spots and prints which ones are **available**.

This class ensures **centralized control of parking operations** while following the **singleton approach**, preventing multiple instances.

---

### **Main Program (Testing the Functionality)**

The **main program** simulates the parking lot operations.

1. A **parking lot with 10 spots** is created.
2. Vehicles (cars and motorcycles) are instantiated with unique **license plates**.
3. Vehicles are parked at **specific spots**.
4. If a vehicle is parked in an **occupied spot**, an error is raised.
5. Vehicles are unparked to **free up spots**.
6. The updated parking lot availability is displayed **after every operation**.


```
# Does the parking have multiple floors ? No

# Any particular number of parking spots  - 10

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
```