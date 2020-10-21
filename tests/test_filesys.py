import unittest

from typing import List
from lib.filesys import File, Directory

def build_data():
    readme = File(name = "readme.txt", size = 1)
    config = File(name = "config.xml", size = 2)
    build  = File(name = "build.bat", size = 3)
    src = Directory(name = "src", size = 10, subitems = [readme, config, build])
    bin = Directory(name = "bin", size = 10, subitems = [])
    root = Directory(name = "root", size = 5, subitems = [src, bin])
    return readme, config, build, src, bin, root

class TestFileSys(unittest.TestCase):
    #
    def test_totalsize(self):
        readme, config, build, src, bin, root = build_data()
        def fFile(item: File):
            return item.size
        def fDir(name: str, size: int, subres: List[int]):
            return size + sum(subres)
        self.assertEqual(readme.cata(fFile, fDir), 1)
        self.assertEqual(src.cata(fFile, fDir), 16)
        self.assertEqual(root.cata(fFile, fDir), 31)


if __name__ == "__main__":
    unittest.main()