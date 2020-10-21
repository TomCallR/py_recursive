from typing import List

class FileSysItem:
    #
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    #
    def __str__():
        raise NotImplementedError
    #
    def cata(self, fFile, fDir):
        raise NotImplementedError
    #
    def total_size(self):
        def file_size(item: File):
            return item.size
        def dir_size(name: str, size: int, subres: List[int]):
            return size + sum(subres)
        return self.cata(file_size, dir_size)


class File(FileSysItem):
    #
    def __init__(self, name: str, size: int):
        super().__init__(name, size)
    #
    def cata(self, fFile, fDir):
        return fFile(self)
    
class Directory(FileSysItem):
    def __init__(self, name: str, size: int, subitems: List[FileSysItem]):
        super().__init__(name, size)
        self.subitems = subitems
    #
    def cata(self, fFile, fDir):
        subresults = [item.cata(fFile, fDir) for item in self.subitems]
        return fDir(self.name, self.size, subresults)

if __name__ == "__main__":
    print("Hello world")