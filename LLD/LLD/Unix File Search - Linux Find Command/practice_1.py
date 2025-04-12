# Creating the File Class
class File():
    def __init__(self, name, size, parent = None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.isDirectory = False if "." in name else True
        self.extension = name.split(".")[-1] if "." in name else ""
    
    # Creating the get_full_path method
    def get_full_path(self):
        if self.parent:
            return self.parent.get_full_path() + "/" + self.name
        return self.name
    
    # Creating the __repr__ method
    def __repr__(self):
        return f"\nFie Name: {self.name}\nFile Location: {self.get_full_path()}\n"

# Creating the Filter Class
class Filter():
    def apply(self, file):
        pass

# Creating the MinSizeFilter class
class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size
    
    # Creating the apply method
    def apply(self, file):
        return file.size >= self.size

# Creating the ExtensionFilter Class
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension
    
    # Creating the apply method
    def apply(self, file):
        return file.extension == self.extension
    
# Creating the FileSystem Class
class FileSystem():
    def __init__(self):
        self.filters = []

    # Creating the addFile method
    def addFile(self, givenfilter):
        if isinstance(givenfilter, Filter):
            self.filters.append(givenfilter)
    
    # Creating the applyORFiltering method that uses DFS
    def applyORFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for filter in self.filters:
                    if filter.apply(root):
                        result.append(root)
                        return
        result = []
        dfs(root, result)
        return result

    # Creating the applyORFiltering method that uses DFS
    def applyANDFiltering(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for filter in self.filters:
                    if not filter.apply(root):
                        return
                result.append(root)
        result = []
        dfs(root, result)
        return result
    

# Creating the Main funtion
if __name__ =="__main__":

    # Creating root Directory
    root = File("root", 300)

    # Creating the subdirectories
    sub1 = File("fiction", 100, root)
    sub2 = File("action", 100, root)
    root.children = [sub1, sub2]

    # Adding files in the subdirectories
    fic_1 = File("naruto.txt", 20, sub1)
    fic_2 = File("harry_potter.mp4", 10, sub1)
    fic_3 = File("ironman.txt", 30, sub1)
    fic_4 = File("batman.mp4", 15, sub1)
    fic_5 = File("superman.txt", 20, sub1)
    sub1.children = [fic_1, fic_2, fic_3, fic_4, fic_5]

    # Adding files in the subdirectories 
    ac_1 = File("avengers.txt", 20, sub2)
    ac_2 = File("justice_league.mp4", 10, sub2)
    ac_3 = File("thor.txt", 30, sub2)
    ac_4 = File("aquaman.mp4", 25, sub2)
    ac_5 = File("superman.txt", 20, sub2)
    sub2.children = [ac_1, ac_2, ac_3, ac_4, ac_5]

    # Creating the Filters
    min_size_filter = MinSizeFilter(20)
    extension_filter = ExtensionFilter("mp4")

    # Creating the FileSystem
    fs = FileSystem()
    fs.addFile(min_size_filter)
    fs.addFile(extension_filter)

    # Applying OR Filtering
    print("OR Filtering")
    print(fs.applyORFiltering(root))

    # Applying AND Filtering
    print("AND Filtering")
    print(fs.applyANDFiltering(root))