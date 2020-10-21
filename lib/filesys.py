from typing import List

class FileSys:
    #
    def __str__():
        raise NotImplementedError
    #
    def cata(self, fFile, fDir):
        raise NotImplementedError

class File(FileSys):
    #
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    #
    def cata(self, fFile, fDir):
        return fFile(self)
    
class Directory(FileSys):
    def __init__(self, name: str, size: int, subitems: List[FileSys]):
        self.name = name
        self.size = size
        self.subitems = subitems
    #
    def cata(self, fFile, fDir):
        subresults = [item.cata(fFile, fDir) for item in self.subitems]
        return fDir(self.name, self.size, subresults)

if __name__ == "__main__":
    print("Hello world")