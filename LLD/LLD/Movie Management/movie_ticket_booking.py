from datetime import datetime, timedelta
from typing import List, Dict
from enum import Enum
import itertools

# Enum for Seat Type
class SeatType(Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"

# Enum for Seat Status
class SeatStatus(Enum):
    AVAILABLE = "AVAILABLE"
    BOOKED = "BOOKED"

# Enum for Booking Status
class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

# Movie Class
class Movie:
    def __init__(self, movie_id: str, title: str, description: str, duration_in_minutes: int):
        self._id = movie_id
        self._title = title
        self._description = description
        self._duration_in_minutes = duration_in_minutes

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def duration_in_minutes(self) -> int:
        return self._duration_in_minutes

# Theater Class
class Theater:
    def __init__(self, theater_id: str, name: str, location: str, shows: List):
        self._id = theater_id
        self._name = name
        self._location = location
        self._shows = shows

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def shows(self) -> List:
        return self._shows

# Seat Class
class Seat:
    def __init__(self, seat_id: str, row: int, column: int, seat_type: SeatType, price: float, status: SeatStatus):
        self._id = seat_id
        self._row = row
        self._column = column
        self._type = seat_type
        self._price = price
        self._status = status

    @property
    def id(self) -> str:
        return self._id

    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @property
    def type(self) -> SeatType:
        return self._type

    @property
    def price(self) -> float:
        return self._price

    @property
    def status(self) -> SeatStatus:
        return self._status

    @status.setter
    def status(self, status: SeatStatus):
        self._status = status

# Show Class
class Show:
    def __init__(self, show_id: str, movie: Movie, theater: Theater, start_time: datetime, end_time: datetime, seats: Dict[str, Seat]):
        self._id = show_id
        self._movie = movie
        self._theater = theater
        self._start_time = start_time
        self._end_time = end_time
        self._seats = seats

    @property
    def id(self) -> str:
        return self._id

    @property
    def movie(self) -> Movie:
        return self._movie

    @property
    def theater(self) -> Theater:
        return self._theater

    @property
    def start_time(self) -> datetime:
        return self._start_time

    @property
    def end_time(self) -> datetime:
        return self._end_time

    @property
    def seats(self) -> Dict[str, Seat]:
        return self._seats

# User Class
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self._id = user_id
        self._name = name
        self._email = email

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

# Booking Class
class Booking:
    def __init__(self, booking_id: str, user: User, show: Show, seats: List[Seat], total_price: float, status: BookingStatus):
        self._id = booking_id
        self._user = user
        self._show = show
        self._seats = seats
        self._total_price = total_price
        self._status = status

    @property
    def id(self) -> str:
        return self._id

    @property
    def user(self) -> User:
        return self._user

    @property
    def show(self) -> Show:
        return self._show

    @property
    def seats(self) -> List[Seat]:
        return self._seats

    @property
    def total_price(self) -> float:
        return self._total_price

    @property
    def status(self) -> BookingStatus:
        return self._status

    @status.setter
    def status(self, status: BookingStatus):
        self._status = status

# MovieTicketBookingSystem (Singleton)
class MovieTicketBookingSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.movies = []
            cls._instance.theaters = []
            cls._instance.shows = {}
            cls._instance.bookings = {}
            cls._instance.booking_counter = itertools.count(1)
        return cls._instance

    @staticmethod
    def get_instance():
        if MovieTicketBookingSystem._instance is None:
            MovieTicketBookingSystem()
        return MovieTicketBookingSystem._instance

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def add_theater(self, theater: Theater):
        self.theaters.append(theater)

    def add_show(self, show: Show):
        self.shows[show.id] = show

    def get_show(self, show_id: str) -> Show:
        return self.shows.get(show_id)

    def book_tickets(self, user: User, show: Show, selected_seats: List[Seat]) -> Booking:
        if all(seat.status == SeatStatus.AVAILABLE for seat in selected_seats):
            for seat in selected_seats:
                seat.status = SeatStatus.BOOKED
            total_price = sum(seat.price for seat in selected_seats)
            booking_id = f"BKG{datetime.now().strftime('%Y%m%d%H%M%S')}{next(self._instance.booking_counter):06d}"
            booking = Booking(booking_id, user, show, selected_seats, total_price, BookingStatus.PENDING)
            self.bookings[booking_id] = booking
            return booking
        return None

    def confirm_booking(self, booking_id: str):
        booking = self.bookings.get(booking_id)
        if booking and booking.status == BookingStatus.PENDING:
            booking.status = BookingStatus.CONFIRMED

    def cancel_booking(self, booking_id: str):
        booking = self.bookings.get(booking_id)
        if booking and booking.status != BookingStatus.CANCELLED:
            booking.status = BookingStatus.CANCELLED
            for seat in booking.seats:
                seat.status = SeatStatus.AVAILABLE

# Demo Execution
if __name__ == "__main__":
    booking_system = MovieTicketBookingSystem.get_instance()

    # Add movies
    movie1 = Movie("M1", "Movie 1", "Description 1", 120)
    movie2 = Movie("M2", "Avengers", "Description 1", 120)
    movie3 = Movie("M3", "Iron Man", "Description 1", 120)
    movie4 = Movie("M4", "BatMan", "Description 1", 120)
    booking_system.add_movie(movie1)
    booking_system.add_movie(movie2)
    booking_system.add_movie(movie3)
    booking_system.add_movie(movie4)

    # Add theaters
    theater1 = Theater("T1", "Theater 1", "Location 1", [])
    theater2 = Theater("T2", "Theater 2", "Location 2", [])
    booking_system.add_theater(theater1)
    booking_system.add_theater(theater2)

    # Create seats
    seats1 = {
        f"{r}-{c}": Seat(f"{r}-{c}", r, c, SeatType.PREMIUM if r <= 2 else SeatType.NORMAL, 
                         150.0 if r <= 2 else 100.0, SeatStatus.AVAILABLE)
        for r in range(1, 6) for c in range(1, 6)
    }

    seats2 = {
        f"{r}-{c}": Seat(f"{r}-{c}", r, c, SeatType.PREMIUM if r <= 2 else SeatType.NORMAL, 
                         180.0 if r <= 2 else 120.0, SeatStatus.AVAILABLE)
        for r in range(1, 6) for c in range(1, 6)
    }

    # Add shows (Each show corresponds to a movie-theater combination)
    show1 = Show("S1", movie1, theater1, datetime.now(), datetime.now() + timedelta(minutes=120), seats1)
    show2 = Show("S2", movie3, theater1, datetime.now(), datetime.now() + timedelta(minutes=120), seats2)
    show3 = Show("S3", movie2, theater2, datetime.now(), datetime.now() + timedelta(minutes=120), seats1)
    show4 = Show("S4", movie4, theater2, datetime.now(), datetime.now() + timedelta(minutes=120), seats2)

    booking_system.add_show(show1)
    booking_system.add_show(show2)
    booking_system.add_show(show3)
    booking_system.add_show(show4)

    # List of users, their selected show, and their selected seats
    users_booking_info = [
        (User("U1", "John Doe", "john@example.com"), show1, ["1-1", "1-2"]),
        (User("U2", "Arun", "arun@example.com"), show3, ["1-3", "1-4"]),  # Booking for a different movie
        (User("U3", "Sandy", "sandy@example.com"), show4, ["1-4", "1-5"]),  # Booking for yet another movie
    ]

    # Process each user's booking
    for user, show, seat_ids in users_booking_info:
        selected_seats = [show.seats[seat_id] for seat_id in seat_ids if seat_id in show.seats]
        booking = booking_system.book_tickets(user, show, selected_seats)

        if booking:
            booking_system.confirm_booking(booking.id)

            # Printing detailed booking information
            print("\n🎟️ Booking Confirmation 🎟️")
            print(f"✅ Booking ID: {booking.id}")
            print(f"👤 User: {user.name} ({user.email})")
            print(f"🎬 Movie: {booking.show.movie.title}")
            print(f"🎭 Theater: {booking.show.theater.name}, Location: {booking.show.theater.location}")
            print(f"🕒 Show Timing: {booking.show.start_time.strftime('%Y-%m-%d %H:%M:%S')} to {booking.show.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"🎫 Number of Seats Booked: {len(booking.seats)}")
            print(f"💺 Seat Details: {', '.join(seat.id for seat in booking.seats)}")
            print(f"💰 Total Price: ${booking.total_price:.2f}")
            print(f"📌 Booking Status: {booking.status.value}")

        else:
            print(f"\n⚠️ Booking failed for {user.name}. Selected seats are not available.")
