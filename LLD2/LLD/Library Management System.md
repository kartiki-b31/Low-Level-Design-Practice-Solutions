
## Requirements

1. The library management system should allow librarians to manage books, members, and borrowing activities.
2. The system should support adding, updating, and removing books from the library catalog.
3. Each book should have details such as title, author, ISBN, publication year, and availability status.
4. The system should allow members to borrow and return books.
5. Each member should have details such as name, member ID, contact information, and borrowing history.
6. The system should enforce borrowing rules, such as a maximum number of books that can be borrowed at a time and loan duration.
7. The system should handle concurrent access to the library catalog and member records.
8. The system should be extensible to accommodate future enhancements and new features.

## Classes, Interfaces and Enumerations

1. The **Book** class represents a book in the library catalog, with properties such as ISBN, title, author, publication year, and availability status.
2. The **Member** class represents a library member, with properties like member ID, name, contact information, and a list of borrowed books.
3. The **LibraryManager** class is the core of the library management system and follows the Singleton pattern to ensure a single instance of the library manager.
4. The LibraryManager class uses concurrent data structures (ConcurrentHashMap) to handle concurrent access to the library catalog and member records.
5. The LibraryManager class provides methods for adding and removing books, registering and unregistering members, borrowing and returning books, and searching for books based on keywords.
6. The **LibraryManagementSystemDemo** class serves as the entry point of the application and demonstrates the usage of the library management system.


---

## **1️⃣ Why These Classes?**

To build an efficient and organized system, we structured our design using **three main classes**:

- **Book** → Represents a single book in the library.
- **Member** → Represents a library user who borrows books.
- **LibraryManager** → A singleton class that acts as the central system for managing books and members.

Each class has a **clear responsibility** to keep the code modular and maintainable. Let’s go into each one.

---

## **2️⃣ The Book Class – Representation of Library Books**

The **`Book`** class is responsible for storing information about a book. Since every book in a library has fixed attributes such as **ISBN, title, author, publication year, and availability status**, we encapsulate these details within the `Book` class.

- The **ISBN** (International Standard Book Number) uniquely identifies a book.
- The **title, author, and publication year** provide details about the book.
- The **availability status** keeps track of whether the book is borrowed or available.

All attributes are **marked as private** (`self._isbn`, `self._title`, etc.), ensuring encapsulation so that they cannot be modified directly from outside the class. Instead, we use **getter methods (`@property`)** to access them, and for `available`, we provide a **setter method** (`@available.setter`) to allow changes when the book is borrowed or returned.

The **relationship of this class** with others is that **books are borrowed by members**, and the **LibraryManager** keeps a record of all books in the library.

---

## **3️⃣ The Member Class – Representation of Library Users**

The **`Member`** class represents people who borrow books. Each member has:

- A **unique member ID** (`member_id`).
- A **name** and **contact details** (`contact_info`).
- A list of **borrowed books** (`_borrowed_books`), which keeps track of the books currently checked out.

The **relationship of this class** is that each **Member can borrow multiple books**, but the number of borrowed books should not exceed the allowed limit (defined in `LibraryManager`).

We provide two key functions:

- `borrow_book(book: Book)`: Adds the book to the member’s borrowed list.
- `return_book(book: Book)`: Removes the book from the borrowed list.

The `borrow_book` and `return_book` methods **interact with the Book class** because they need to update the availability of books. This ensures that a book cannot be borrowed by multiple people simultaneously.

---

## **4️⃣ The LibraryManager Class – The Core of the System**

### **Why Singleton?**

The **LibraryManager** class is designed as a **singleton**, which means there can only be **one instance** of it throughout the system. This ensures:

1. A **single source of truth** for managing books and members.
2. Consistency in book availability and member records.
3. Prevents accidental creation of multiple instances that could lead to inconsistent data.

To implement this, we override the `__new__` method:

- The **first time** `LibraryManager()` is called, it **creates an instance** (`_instance`).
- Subsequent calls return the **same instance**, ensuring a **global, shared library system**.

### **Responsibilities of LibraryManager**

The **LibraryManager** handles the core functionalities:

1. **Managing Books**
    
    - `add_book(book: Book)`: Adds a book to the catalog (stored in a dictionary using ISBN as the key).
    - `remove_book(isbn: str)`: Deletes a book from the catalog.
    - `get_book(isbn: str)`: Retrieves book details by ISBN.
2. **Managing Members**
    
    - `register_member(member: Member)`: Registers a new member.
    - `unregister_member(member_id: str)`: Removes a member.
    - `get_member(member_id: str)`: Fetches details of a member.
3. **Handling Borrowing & Returning**
    
    - `borrow_book(member_id: str, isbn: str)`:
        
        - Checks if the member exists.
        - Checks if the book is available.
        - Ensures the member has not exceeded the borrowing limit (`MAX_BOOKS_PER_MEMBER`).
        - Updates the book’s availability status and adds it to the member’s list.
    - `return_book(member_id: str, isbn: str)`:
        
        - Ensures the book and member exist.
        - Updates the book’s availability status when returned.
4. **Searching for Books**
    
    - `search_books(keyword: str)`: Searches for books by title or author and returns a list of matching results.

The **LibraryManager class directly interacts with both the `Book` and `Member` classes**, ensuring all data is updated correctly.

---

## **5️⃣ Where Are Objects Created?**

The objects for `Book`, `Member`, and `LibraryManager` are instantiated under the **`if __name__ == "__main__"`** block.

1. **Creating the Singleton Instance of LibraryManager**
    
    - `library_manager = LibraryManager.get_instance()`
    - This ensures that all future calls refer to the same library system.
2. **Creating Books**
    
    - We instantiate **three books** (`Book("ISBN1", "Book 1", "Author 1", 2020)`, etc.) and add them to the `library_manager` catalog.
3. **Registering Members**
    
    - We instantiate **two members** (`Member("M1", "John Doe", "john@example.com")`, etc.) and register them in `library_manager`.
4. **Performing Actions**
    
    - Members **borrow and return books** through `borrow_book()` and `return_book()`.
    - A **search operation** is performed to retrieve books matching a keyword.

By placing these operations in the **main block (`if __name__ == "__main__"`)**, we separate logic from the class definitions, ensuring better structure.

---

## **6️⃣ Why We Chose This Approach?**

1. **Encapsulation & Data Integrity**
    
    - By keeping attributes private (`self._attribute`), we prevent accidental modifications.
    - Getters (`@property`) allow controlled access, ensuring the correct behavior of book availability.
2. **Object-Oriented Design & Relationships**
    
    - **Book ↔ Member Relationship** → A book can only be borrowed by one member at a time.
    - **LibraryManager as Central Control** → It acts as the **middleware** between Books and Members.
3. **Scalability & Maintainability**
    
    - The Singleton pattern ensures that multiple users interact with the **same library system**, preventing conflicts.
    - The modular class structure allows **easy future modifications** (e.g., adding e-books, tracking due dates).
4. **Concurrency Handling**
    
    - By maintaining books in a **dictionary (`catalog`)**, retrieval is **fast and efficient**.
    - The system supports **multiple members borrowing books simultaneously**, avoiding global locks.


```
from typing import List, Dict

  

# Book Class

class Book:

    def __init__(self, isbn: str, title: str, author: str, publication_year: int):

        self._isbn = isbn

        self._title = title

        self._author = author

        self._publication_year = publication_year

        self._available = True

  

    @property

    def isbn(self) -> str:

        return self._isbn

  

    @property

    def title(self) -> str:

        return self._title

  

    @property

    def author(self) -> str:

        return self._author

  

    @property

    def publication_year(self) -> int:

        return self._publication_year

  

    @property

    def available(self) -> bool:

        return self._available

  

    @available.setter

    def available(self, available: bool):

        self._available = available

  
  

# Member Class

class Member:

    def __init__(self, member_id: str, name: str, contact_info: str):

        self._member_id = member_id

        self._name = name

        self._contact_info = contact_info

        self._borrowed_books = []

  

    @property

    def member_id(self) -> str:

        return self._member_id

  

    @property

    def name(self) -> str:

        return self._name

  

    @property

    def contact_info(self) -> str:

        return self._contact_info

  

    @property

    def borrowed_books(self) -> List[Book]:

        return self._borrowed_books

  

    def borrow_book(self, book: Book):

        self._borrowed_books.append(book)

  

    def return_book(self, book: Book):

        self._borrowed_books.remove(book)

  
  

# LibraryManager Class (Singleton)

class LibraryManager:

    _instance = None

  

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.catalog = {}

            cls._instance.members = {}

            cls._instance.MAX_BOOKS_PER_MEMBER = 5

            cls._instance.LOAN_DURATION_DAYS = 14

        return cls._instance

  

    @staticmethod

    def get_instance():

        if LibraryManager._instance is None:

            LibraryManager()

        return LibraryManager._instance

  

    def add_book(self, book: Book):

        self.catalog[book.isbn] = book

  

    def remove_book(self, isbn: str):

        self.catalog.pop(isbn, None)

  

    def get_book(self, isbn: str) -> Book:

        return self.catalog.get(isbn)

  

    def register_member(self, member: Member):

        self.members[member.member_id] = member

  

    def unregister_member(self, member_id: str):

        self.members.pop(member_id, None)

  

    def get_member(self, member_id: str) -> Member:

        return self.members.get(member_id)

  

    def borrow_book(self, member_id: str, isbn: str):

        member = self.get_member(member_id)

        book = self.get_book(isbn)

  

        if member and book and book.available:

            if len(member.borrowed_books) < self.MAX_BOOKS_PER_MEMBER:

                member.borrow_book(book)

                book.available = False

                print(f"Book borrowed: {book.title} by {member.name}")

            else:

                print(f"Member {member.name} has reached the maximum number of borrowed books.")

        else:

            print("Book or member not found, or book is not available.")

  

    def return_book(self, member_id: str, isbn: str):

        member = self.get_member(member_id)

        book = self.get_book(isbn)

  

        if member and book:

            member.return_book(book)

            book.available = True

            print(f"Book returned: {book.title} by {member.name}")

        else:

            print("Book or member not found.")

  

    def search_books(self, keyword: str) -> List[Book]:

        matching_books = [book for book in self.catalog.values() if keyword in book.title or keyword in book.author]

        return matching_books

  
  

if __name__ == "__main__":

    library_manager = LibraryManager.get_instance()

  

    # Add books to the catalog

    library_manager.add_book(Book("ISBN1", "Book 1", "Author 1", 2020))

    library_manager.add_book(Book("ISBN2", "Book 2", "Author 2", 2019))

    library_manager.add_book(Book("ISBN3", "Book 3", "Author 3", 2021))

  

    # Register members

    library_manager.register_member(Member("M1", "John Doe", "john@example.com"))

    library_manager.register_member(Member("M2", "Jane Smith", "jane@example.com"))

  

    # Borrow books

    library_manager.borrow_book("M1", "ISBN1")

    library_manager.borrow_book("M2", "ISBN2")

  

    # Return books

    library_manager.return_book("M1", "ISBN1")

  

    # Search books

    search_results = library_manager.search_books("Book")

    print("\nSearch Results:")

    for book in search_results:

        print(f"{book.title} by {book.author}")
```