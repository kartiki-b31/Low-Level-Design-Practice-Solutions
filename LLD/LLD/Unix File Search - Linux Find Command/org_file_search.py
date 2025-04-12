# 📌 Represents a file or directory in the file system
class File():
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent  # Keeps track of the parent directory
        self.children = []  # Stores sub-files/sub-directories
        self.isDirectory = False if "." in name else True  # Determines if it's a directory
        self.extension = name.split(".")[-1] if "." in name else ""  # Extracts file extension

    def get_full_path(self):
        if self.parent:
            return self.parent.get_full_path() + "/" + self.name
        return self.name  # Root case

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
        if isinstance(givenFilter, Filter):  # Ensures only valid filters are added
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
                        result.append(root)  # Add file to result list
                        return  # Stop checking further filters

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
                    if not filter.apply(root):  # If any filter fails, ignore the file
                        return
                result.append(root)  # Add file to result list

        result = []
        dfs(root, result)
        return result


# ✅ **Setup File System**
# Creating the root directory
f1 = File("root", 300)

# 📌 Creating directories inside root
f2 = File("fiction", 100, f1)  # fiction inside root
f3 = File("action", 100, f1)   # action inside root
f4 = File("comedy", 100, f1)   # comedy inside root
f1.children = [f2, f3, f4]  # Adding subdirectories to root

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
f12 = File("Avengers.txt", 12, f3)  # Stored in `action`
f3.children.append(f12)  # Adding file to action directory

# 📌 Files inside comedy directory
f13 = File("BigBangTheory.txt", 4, f4)
f14 = File("AmericanPie.mp3", 6, f4)
f4.children = [f13, f14]


# ✅ **Creating Filters**
greater5 = MinSizeFilter(5)  # Files larger than 5 bytes
txtFilter = ExtentionFilter("txt")  # Only `.txt` files

# ✅ **Initialize FileSystem and Add Filters**
filesystem = FileSystem()
filesystem.addFile(greater5)
filesystem.addFile(txtFilter)

# ✅ **Apply OR Filtering**
print("\n📌 **Files Matching OR Filtering**")
print(filesystem.applyORFiltering(f1))  # Files that match at least one filter

# ✅ **Apply AND Filtering**
print("\n📌 **Files Matching AND Filtering**")
print(filesystem.applyANDFiltering(f1))  # Files that match all filters