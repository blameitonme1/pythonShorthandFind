class findItem:
    shortName = None
    path = None
    cwd = None
    def __init__(self, shorthandName, path, cwd) -> None:
        self.shortName = shorthandName
        self.path = path
        self.cwd = cwd
    def selfDisplay(self):
        print("short name is :" + self.shortName + '\n')
        print(f"current path is {self.path}\n")
        print(f"cwd is {self.cwd}")
