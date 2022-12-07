def read_input(filepath):
    file = open(filepath, 'r')
    return file.readlines()


class DirFile:

    def __init__(self, size, name) -> None:
        self.size = size
        self.name = name

    def get_size(self):
        return self.size

    def __str__(self) -> str:
        return (self.name + " .  " + str(self.size))

class Directory:
    def __init__(self, parent, name) -> None:

        self.name = name
        self.files = []
        self.dirs = []
        self.parent = parent

    def add_file(self, dirFile):
        self.files.append(dirFile)
        
    def add_directory(self, directory):
        self.dirs.append(directory)

    def get_directories(self):
        return self.dirs
    def get_directory_by_name(self,name):
        for d in self.dirs:
            if d.name == name:
                return d

        return None
    
    def get_files(self):
        return self.files

    def get_root(self):
        root = self
        while root.parent is not None:
            root = root.parent
        return root

    def get_size(self):
        size = 0

        for f in self.files:
            size += f.get_size()
        for d in self.dirs:
            size += d.get_size()
        return size

    def printTree(self):
        queue = [self]
        queue += self.get_directories()

        while len(queue) != 0:
            current = queue.pop(0)
            for file in current.get_files():
                print(file)
            for d in current.get_directories():
                d.printTree()




lines = read_input("day7/input.txt")
lines.pop(0)

directory = Directory(None,"/")

for line in lines:
    

    if line[0] == "$": #Command
        args = line.split(" ")
        if args[1] == "cd":
            to_dir = args[2]
        
            if ".." in to_dir: 
                directory = directory.parent
            else:
                print(to_dir)
                directory = directory.get_directory_by_name(to_dir)
        elif args[1] == "ls":
            continue
    else: # List of directory
        splitted = line.split(" ")
        if splitted[0] == "dir":
            directory.add_directory(Directory(directory, splitted[1]))
        else: # File
            [filesize, filename] = splitted
            directory.add_file(DirFile(int(filesize),filename))




# # ------ PART 1 -------
root = directory.get_root()


all_dir_sizes = []
def get_size_and_add(dir, all_dir_sizes):
    tot_size = dir.get_size()
    print(tot_size)
    if(tot_size <= 100000):
        all_dir_sizes.append(tot_size)

    for d in dir.get_directories():
        get_size_and_add(d,all_dir_sizes)


get_size_and_add(root, all_dir_sizes)
sum = 0
for size in all_dir_sizes:
    sum += size

print("PART1: ",sum)



# ------ PART 2 -------
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000
SPACE_USED = root.get_size()

SPACE_AVAILABLE = TOTAL_SPACE-SPACE_USED
SIZE_TO_BE_DELETED = SPACE_NEEDED-SPACE_AVAILABLE



all_dir_sizes = []
def get_possible_dirs(dir, all_dir_sizes):
    tot_size = dir.get_size()

    if(tot_size >= SIZE_TO_BE_DELETED):

        all_dir_sizes.append(tot_size)

    for d in dir.get_directories():
        get_possible_dirs(d,all_dir_sizes)


get_possible_dirs(root, all_dir_sizes)


print("PART2: ",min(all_dir_sizes))