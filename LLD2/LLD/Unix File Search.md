### **Understanding the Overall Structure and Approach**

This program is designed to simulate a **file system** where we can store directories and files, apply filters based on size and extension, and retrieve relevant files based on filtering conditions. The program is built using **object-oriented programming (OOP) principles**, leveraging **classes** to represent different entities such as files, filters, and the file system.

The code is structured into **four main class components**:

1. **`File` Class** - Represents files and directories, storing their attributes such as name, size, and hierarchy.
2. **`Filter` Class (Abstract Concept)** - A base class that is used to define filtering behavior, allowing the creation of specific filtering strategies.
3. **`MinSizeFilter` and `ExtensionFilter` Classes** - These classes inherit from `Filter` and apply specific filtering rules based on file size and file type.
4. **`FileSystem` Class** - Manages a collection of filters and applies them using **depth-first search (DFS)** to retrieve files based on filtering conditions.

Once these classes are defined, the `main` function creates the **directory structure**, initializes the **filtering system**, and applies **both OR and AND filtering** methods.

---

## **Step-by-Step Breakdown of Each Class**

---

### **1️⃣ `File` Class: Representation of a File or Directory**

The `File` class is fundamental to this system, as it represents **both files and directories**. Since files and directories share common properties like **name, size, and hierarchy**, a single class is used to define both.

#### **Why do we need this class?**

- It **stores information** about files and directories.
- It helps in **traversing the hierarchy** using **parent-child relationships**.
- It **differentiates between files and directories** using attributes like `isDirectory`.

#### **Attributes and Their Purpose:**

- `name`: Stores the **file name or directory name**.
- `size`: Represents the **size of the file** (directories also have a size, but it's not used in filtering).
- `parent`: Stores **the reference to the parent directory**, helping in building **full paths**.
- `children`: A **list of child files and directories**, used to **navigate directories**.
- `isDirectory`: A **boolean flag** to differentiate between files (`False`) and directories (`True`).
- `extension`: Extracts the **file type (e.g., .txt, .mp4)** to enable **extension-based filtering**.

#### **Methods in `File` Class:**

- `get_full_path()`: **Recursively constructs the full file path**, appending the parent directory names.
- `__repr__()`: **Provides a readable representation of the file**, showing its name and location.

#### **Where is the `File` Class Used?**

- **When we create directories (`root`, `fiction`, `action`) and files** (`naruto.txt`, `ironman.txt`).
- **When filtering files based on criteria** such as file size or extension.

---

### **2️⃣ `Filter` Class: Abstract Base for Filters**

The `Filter` class is a **base class** that provides a **generic structure for all filtering mechanisms**.

#### **Why do we need an abstract class for filtering?**

- This allows us to **extend functionality** by creating **custom filters** without modifying existing code.
- The **open/closed principle** (OCP) from SOLID design patterns is followed—**we can add new filters without modifying existing code**.
- It ensures that all filters implement the `apply()` method, enforcing **polymorphism**.

#### **Methods in `Filter` Class:**

- `apply(file)`: A **placeholder method** that each subclass must override. This method defines the **filtering logic** for different filtering conditions.

#### **Where is the `Filter` Class Used?**

- It is **not directly used** but serves as a **base class** for the `MinSizeFilter` and `ExtensionFilter` classes.

---

### **3️⃣ `MinSizeFilter` and `ExtensionFilter` Classes: Implementing Filtering Logic**

Both classes **inherit from `Filter`** and implement the `apply()` method, each defining a **specific rule** for filtering.

#### **🟢 `MinSizeFilter` Class (Filtering Based on File Size)**

- This class **stores a size threshold**.
- The `apply()` method **returns `True` if the file’s size is greater than or equal to the threshold**.

#### **🟢 `ExtensionFilter` Class (Filtering Based on File Extension)**

- Stores **a specific file extension**.
- The `apply()` method **checks if the file’s extension matches the required extension**.

#### **Where are these filter classes used?**

- When we **apply filtering** in the `FileSystem` class, it checks if a file meets the conditions of these filters.

---

### **4️⃣ `FileSystem` Class: Applying Filters on the File Hierarchy**

The `FileSystem` class is responsible for:

1. **Storing multiple filtering rules.**
2. **Traversing the file system** using Depth-First Search (DFS).
3. **Applying AND / OR conditions to return matching files.**

#### **Attributes in `FileSystem`:**

- `filters`: A **list of filters** that will be applied to files.

#### **Methods in `FileSystem`:**

1. **`addFile(givenfilter)`**
    
    - Accepts a **filter object** and adds it to the `filters` list.
    - This method allows us to apply **multiple filters**.
2. **`applyORFiltering(root)`**
    
    - Uses **DFS to traverse the directory structure**.
    - Returns **files that match at least one of the filters**.
    - If any filter returns `True`, the file is added to the result.
3. **`applyANDFiltering(root)`**
    
    - Uses **DFS**, but a file **must pass all filters** to be included.
    - If any filter returns `False`, the file is ignored.

---

## **Where Are These Classes Used? (Object Creation & Initialization)**

### **1️⃣ Object Creation (File System Structure)**

- **We create the root directory**: `root = File("root", 300)`.
- **Subdirectories (`fiction` and `action`) are added**: `sub1 = File("fiction", 100, root)`.
- **We add files inside these directories**, e.g., `fic_1 = File("naruto.txt", 20, sub1)`.

### **2️⃣ Initializing Filtering System**

- We create filtering objects:
    - `min_size_filter = MinSizeFilter(20)` → Filters files with **size ≥ 20**.
    - `extension_filter = ExtensionFilter("mp4")` → Filters files with **“.mp4” extension**.
- These filters are added to the `FileSystem` object.

### **3️⃣ Applying Filtering**

- `applyORFiltering(root)`: Returns **files matching at least one filter**.
- `applyANDFiltering(root)`: Returns **files passing all filters**.
---

### **6️⃣ `Search Algorithm - Depth First Search (DFS)`**

The search is implemented using **DFS (Depth First Search)** to traverse the file tree recursively.

- **For OR Filtering (`applyORFiltering`)**:
    
    - If a file meets **at least one filter**, it is added to the result.
    - If a directory is encountered, we recursively search its children.
- **For AND Filtering (`applyANDFiltering`)**:
    
    - If a file meets **all filters**, it is added to the result.
    - If any filter fails, we skip the file.

---

### **🔗 Class Relationships**

- `FileSystem` **manages** file searching.
- `File` **represents** both directories and files, maintaining a **parent-child** hierarchy.
- `Filter` **defines the blueprint** for filtering logic.
- `MinSizeFilter` and `ExtentionFilter` **extend** `Filter` to apply specific filtering conditions.
- `FileSystem` **uses DFS** to traverse `File` objects and apply filters dynamically.

---

### **🎯 Key Design Considerations**

1. **Extensibility**
    - We can add new filters in the future (e.g., `CreatedDateFilter`) without modifying existing classes.
2. **Efficiency (DFS Traversal)**
    - We avoid redundant searches by **pruning early** when filters fail.
3. **Separation of Concerns**
    - **File** stores file system details.
    - **Filters** handle search conditions.
    - **FileSystem** executes search logic.


```
# 📌 Represents a file or directory in the file system
class File():
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent  # Keeps track of the parent directory
        self.children = []  # Stores sub-files/sub-directories
        self.isDirectory = False if "." in name else True  # Determines if it's a directory
        self.extension = name.split(".")[-1] if "." in name else ""  # Extracts file extension

  
    def get_full_path(self):
        if self.parent:
            return self.parent.get_full_path() + "/" + self.name
        return self.name  # Root case

  
    def __repr__(self):
        return f"\nFile Name : {self.name}\nFile Location : {self.get_full_path()}\n"

  

# 📌 Abstract class representing a generic filter
class Filter():

    def apply(self, file):
        pass

  
# 📌 Filters files based on minimum size requirement
class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

  
    def apply(self, file):
        return file.size > self.size

  
# 📌 Filters files based on their extension type
class ExtentionFilter(Filter):
    def __init__(self, extention):
        self.extention = extention

  
    def apply(self, file):
        return file.extension == self.extention

  

# 📌 Manages file searching based on applied filters
class FileSystem():
    def __init__(self):
        self.filters = []

  
    def addFile(self, givenFilter):
        if isinstance(givenFilter, Filter):  # Ensures only valid filters are added
            self.filters.append(givenFilter)

  
    # 📌 Uses DFS (Depth First Search) to apply OR filtering
    def applyORFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                # Recursively explore all children
                for child in root.children:
                    dfs(child, result)
            else:
                # Check if at least one filter matches
                for filter in self.filters:
                    if filter.apply(root):
                        result.append(root)  # Add file to result list
                        return  # Stop checking further filters


        result = []
        dfs(root, result)
        return result

  

    # 📌 Uses DFS (Depth First Search) to apply AND filtering
    def applyANDFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                # Recursively explore all children
                for child in root.children:
                    dfs(child, result)
            else:
                # Check if all filters match
                for filter in self.filters:
                    if not filter.apply(root):  # If any filter fails, ignore the file

                        return
                result.append(root)  # Add file to result list

        result = []
        dfs(root, result)
        return result

  
  

# ✅ **Setup File System**

# Creating the root directory
f1 = File("root", 300)

  
# 📌 Creating directories inside root
f2 = File("fiction", 100, f1)  # fiction inside root
f3 = File("action", 100, f1)   # action inside root
f4 = File("comedy", 100, f1)   # comedy inside root
f1.children = [f2, f3, f4]  # Adding subdirectories to root

  
# 📌 Files inside fiction directory
f5 = File("StarTrek.txt", 4, f2)
f6 = File("StarWars.xml", 10, f2)
f7 = File("JusticeLeague.txt", 15, f2)
f8 = File("Spock.jpg", 1, f2)
f2.children = [f5, f6, f7, f8]

  
# 📌 Files inside action directory
f9 = File("IronMan.txt", 9, f3)
f10 = File("MissionImpossible.rar", 10, f3)
f11 = File("TheLordOfRings.zip", 3, f3)
f3.children = [f9, f10, f11]
  

# ✅ File stored in a different location (Inside `action`, not `fiction`)
f12 = File("Avengers.txt", 12, f3)  # Stored in `action`
f3.children.append(f12)  # Adding file to action directory

  
# 📌 Files inside comedy directory
f13 = File("BigBangTheory.txt", 4, f4)
f14 = File("AmericanPie.mp3", 6, f4)
f4.children = [f13, f14]

  
# ✅ **Creating Filters**
greater5 = MinSizeFilter(5)  # Files larger than 5 bytes
txtFilter = ExtentionFilter("txt")  # Only `.txt` files

  
# ✅ **Initialize FileSystem and Add Filters**
filesystem = FileSystem()
filesystem.addFile(greater5)
filesystem.addFile(txtFilter)

  

# ✅ **Apply OR Filtering**
print("\n📌 **Files Matching OR Filtering**")
print(filesystem.applyORFiltering(f1))  # Files that match at least one filter

  
# ✅ **Apply AND Filtering**
print("\n📌 **Files Matching AND Filtering**")
print(filesystem.applyANDFiltering(f1))  # Files that match all filters

```