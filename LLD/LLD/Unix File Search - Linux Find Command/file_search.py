from abc import ABC, abstractmethod
from collections import deque
from typing import List

# File class
class File:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.is_directory = False if '.' in name else True
        self.extension = name.split(".")[-1] if '.' in name else ""

    def get_full_path(self):
        if self.parent:
            return self.parent.get_full_path() + "/" + self.name
        return self.name  # Root

    def __repr__(self):
        return self.get_full_path()

# Abstract Filter
class Filter(ABC):
    @abstractmethod
    def apply(self, file):
        pass

# Filters
class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size >= self.size  # Fix: Include equal-sized files

class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension

# NOT Filter (Negation)
class NotFilter(Filter):
    def __init__(self, filter_obj):
        self.filter_obj = filter_obj

    def apply(self, file):
        return not self.filter_obj.apply(file)

# AND Filter
class AndFilter(Filter):
    def __init__(self, filters: List[Filter]):
        self.filters = filters

    def apply(self, file):
        return all(filter_obj.apply(file) for filter_obj in self.filters)

# OR Filter
class OrFilter(Filter):
    def __init__(self, filters: List[Filter]):
        self.filters = filters

    def apply(self, file):
        return any(filter_obj.apply(file) for filter_obj in self.filters)

# LinuxFindCommand
class LinuxFind:
    def __init__(self):
        self.filters = []

    def add_filter(self, given_filter):
        if isinstance(given_filter, Filter):
            self.filters.append(given_filter)

    def search(self, root, filter_type="AND"):
        found_files = []
        queue = deque([root])

        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                is_valid = any(f.apply(curr_root) for f in self.filters) if filter_type == "OR" else all(f.apply(curr_root) for f in self.filters)
                if is_valid:
                    found_files.append(curr_root)
                    print(curr_root)

        return found_files

# Setup File System
f1 = File("root", 300)

# Create directories
f2 = File("fiction", 100, f1)  # fiction inside root
f3 = File("action", 100, f1)   # action inside root
f4 = File("comedy", 100, f1)   # comedy inside root
f1.children = [f2, f3, f4]

# Files inside fiction
f5 = File("StarTrek.txt", 4, f2)
f6 = File("StarWars.xml", 10, f2)
f7 = File("JusticeLeague.txt", 15, f2)
f8 = File("Spock.jpg", 1, f2)
f2.children = [f5, f6, f7, f8]

# Files inside action
f9 = File("IronMan.txt", 9, f3)
f10 = File("MissionImpossible.rar", 10, f3)
f11 = File("TheLordOfRings.zip", 3, f3)
f3.children = [f9, f10, f11]

# ✅ File stored in a different location (Inside `action`, not `fiction`)
f12 = File("Avengers.txt", 12, f3)  # Stored in `action`
f3.children.append(f12)  # Adding file to action directory

# Files inside comedy
f13 = File("BigBangTheory.txt", 4, f4)
f14 = File("AmericanPie.mp3", 6, f4)
f4.children = [f13, f14]

# Apply Filters
greater5_filter = MinSizeFilter(5)
txt_filter = ExtensionFilter("txt")

finder = LinuxFind()
finder.add_filter(greater5_filter)
finder.add_filter(txt_filter)

print("\n📌 **Files Matching OR Filtering**")
print(finder.search(f1, "OR"))  # OR filtering

print("\n📌 **Files Matching AND Filtering**")
print(finder.search(f1, "AND"))  # AND filtering    