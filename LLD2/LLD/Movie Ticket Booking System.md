## Requirements

1. The system should allow users to view the list of movies playing in different theaters.
2. Users should be able to select a movie, theater, and show timing to book tickets.
3. The system should display the seating arrangement of the selected show and allow users to choose seats.
4. Users should be able to make payments and confirm their booking.
5. The system should handle concurrent bookings and ensure seat availability is updated in real-time.
6. The system should support different types of seats (e.g., normal, premium) and pricing.
7. The system should allow theater administrators to add, update, and remove movies, shows, and seating arrangements.
8. The system should be scalable to handle a large number of concurrent users and bookings.

## Classes, Interfaces and Enumerations

1. The **Movie** class represents a movie with properties such as ID, title, description, and duration.
2. The **Theater** class represents a theater with properties such as ID, name, location, and a list of shows.
3. The **Show** class represents a movie show in a theater, with properties such as ID, movie, theater, start time, end time, and a map of seats.
4. The **Seat** class represents a seat in a show, with properties such as ID, row, column, type, price, and status.
5. The **SeatType** enum defines the different types of seats (normal or premium).
6. The **SeatStatus** enum defines the different statuses of a seat (available or booked).
7. The **Booking** class represents a booking made by a user, with properties such as ID, user, show, selected seats, total price, and status.
8. The **BookingStatus** enum defines the different statuses of a booking (pending, confirmed, or cancelled).
9. The **User** class represents a user of the booking system, with properties such as ID, name, and email.
10. The **MovieTicketBookingSystem** class is the main class that manages the movie ticket booking system. It follows the Singleton pattern to ensure only one instance of the system exists.
11. The MovieTicketBookingSystem class provides methods for adding movies, theaters, and shows, as well as booking tickets, confirming bookings, and cancelling bookings.
12. Multi-threading is achieved using concurrent data structures such as ConcurrentHashMap to handle concurrent access to shared resources like shows and bookings.
13. The **MovieTicketBookingDemo** class demonstrates the usage of the movie ticket booking system by adding movies, theaters, shows, booking tickets, and confirming or cancelling bookings.


---

To build a **scalable** and **maintainable** ticket booking system, we define different **real-world entities** as classes:

### **🎬 Movie Class**

- Represents **a movie** that can be screened in theaters.
- Attributes:
    - `movie_id`: Unique identifier for the movie.
    - `title`: Name of the movie.
    - `description`: Brief details about the movie.
    - `duration_in_minutes`: Length of the movie in minutes.

👉 **Why do we need a separate `Movie` class?**

- A movie is a distinct entity that is **reused** across multiple shows in different theaters.
- Helps us **avoid redundant data** and ensures modularity.

---

### **🏛️ Theater Class**

- Represents **a movie theater** where shows take place.
- Attributes:
    - `theater_id`: Unique identifier for the theater.
    - `name`: Name of the theater.
    - `location`: Where the theater is situated.
    - `shows`: A list of shows being played in that theater.

👉 **Why do we need a `Theater` class?**

- Multiple theaters exist, and each theater **screens multiple movies** at different times.
- The `Theater` class ensures that we can **manage multiple locations and their respective schedules** efficiently.

---

### **🎭 Show Class**

- Represents **a specific screening of a movie** at a particular theater.
- Attributes:
    - `show_id`: Unique identifier for the show.
    - `movie`: The movie being played.
    - `theater`: The theater where the movie is screened.
    - `start_time`: Show's starting time.
    - `end_time`: Show's ending time.
    - `seats`: A dictionary mapping seat IDs to seat objects.

👉 **Why do we need a `Show` class?**

- A movie can have **multiple screenings at different times and locations**.
- The `Show` class **links** a specific movie to a theater, ensuring proper scheduling.

---

### **💺 Seat Class**

- Represents **a seat in a theater for a particular show**.
- Attributes:
    - `seat_id`: Unique identifier for the seat (row-column format).
    - `row`, `column`: Position of the seat in the theater.
    - `seat_type`: Can be `NORMAL` or `PREMIUM`.
    - `price`: Cost of booking this seat.
    - `status`: Can be `AVAILABLE` or `BOOKED`.

👉 **Why do we need a `Seat` class?**

- Each show has **multiple seats**, and their **availability status changes dynamically**.
- Helps in **handling seat pricing and booking status efficiently**.

---

### **👤 User Class**

- Represents **a customer using the booking system**.
- Attributes:
    - `user_id`: Unique identifier for the user.
    - `name`: Name of the user.
    - `email`: Contact email.

👉 **Why do we need a `User` class?**

- To associate **each booking with a specific user**.
- Helps in **personalized booking experiences** and managing user data.

---

### **🎟️ Booking Class**

- Represents **a confirmed or pending ticket reservation**.
- Attributes:
    - `booking_id`: Unique identifier for the booking.
    - `user`: The user who made the booking.
    - `show`: The show for which tickets are booked.
    - `seats`: A list of booked seats.
    - `total_price`: Total cost of booking.
    - `status`: Can be `PENDING`, `CONFIRMED`, or `CANCELLED`.

👉 **Why do we need a `Booking` class?**

- Maintains a **record of ticket reservations**.
- Tracks **which seats are booked and by whom**.

---

## **2️⃣ Enums for Standardized Categorization**

We use **Enumerations (`Enum`)** to define **predefined categories**, ensuring **data consistency**.

### **SeatType Enum**

Defines seat classifications:

- `NORMAL`
- `PREMIUM`

### **SeatStatus Enum**

Defines seat availability:

- `AVAILABLE`
- `BOOKED`

### **BookingStatus Enum**

Defines booking lifecycle:

- `PENDING`
- `CONFIRMED`
- `CANCELLED`

👉 **Why do we need Enums?**

- Prevents errors caused by inconsistent status values.
- Enforces **strict categorization**.

---

## **3️⃣ Implementing the Core System: Singleton MovieTicketBookingSystem**

The **MovieTicketBookingSystem** is the **central class** managing:

1. Movies
2. Theaters
3. Shows
4. Bookings

This follows the **Singleton Pattern**, ensuring **only one instance** of the system exists.

### **Why use a Singleton?**

- Prevents multiple instances of the booking system.
- Ensures **consistent data management** across the application.

### **Key Functions:**

#### 🔹 `add_movie()`

Adds a new movie to the system.

#### 🔹 `add_theater()`

Registers a theater.

#### 🔹 `add_show()`

Schedules a movie in a theater.

#### 🔹 `book_tickets()`

Handles **ticket reservations**:

- Checks **seat availability**.
- Marks seats as **BOOKED**.
- Generates a **unique booking ID**.

#### 🔹 `confirm_booking()`

Finalizes a **pending reservation**.

#### 🔹 `cancel_booking()`

Cancels a booking, making seats **available again**.

---

## **4️⃣ Creating Objects and Executing the Booking System**

Inside the `if __name__ == "__main__":` block, we:

1️⃣ **Initialize the Booking System**  
2️⃣ **Create Movies and Theaters**  
3️⃣ **Define Seat Arrangements**  
4️⃣ **Schedule Movie Shows**  
5️⃣ **Simulate User Booking**

---

## **5️⃣ Booking Process Flow**

### **🔹 Step 1: A user selects a movie and show**

- We create a `User` object representing **John Doe**.
- We select a **specific show** from the available shows.

### **🔹 Step 2: The user selects seats**

- The user chooses **seat 1-1 and 1-2**.

### **🔹 Step 3: Booking is processed**

- The system **checks seat availability**.
- If seats are **available**, a **new Booking object** is created.
- The total **ticket price is calculated**.

### **🔹 Step 4: Confirming the booking**

- The system **confirms** the booking and updates **seat statuses**.

---

## **6️⃣ Handling Edge Cases**

- If a seat is **already booked**, the system **prevents duplicate reservations**.
- If a user **cancels a booking**, the system **frees up the seats**.
- The **Singleton pattern ensures data consistency**.

---

## **7️⃣ Final Booking Confirmation Output**

Once a **successful booking** occurs, we print:

yaml

CopyEdit

`🎟️ Booking Confirmation 🎟️ ✅ Booking ID: BKG202502111234560001 👤 User: John Doe (john@example.com) 🎬 Movie: Movie 1 🎭 Theater: Theater 1, Location: Location 1 🕒 Show Timing: 2025-02-11 12:34:56 to 2025-02-11 14:34:56 🎫 Number of Seats Booked: 2 💺 Seat Details: 1-1, 1-2 💰 Total Price: $300.00 📌 Booking Status: CONFIRMED`

---

## **8️⃣ Why This Design?**

1️⃣ **Scalability** – Can handle **multiple users and concurrent bookings**.  
2️⃣ **Maintainability** – **Each entity has its own class**, making modifications easier.  
3️⃣ **Data Integrity** – Uses **singleton for system consistency**.  
4️⃣ **Realism** – Implements **real-world constraints like seat availability, pricing, and booking confirmation**.