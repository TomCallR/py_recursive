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
        self.assertEqual(readme.total_size(), 1)
        self.assertEqual(src.total_size(), 16)
        self.assertEqual(root.total_size(), 31)
    #
    def test_largestfile(self):
        readme, config, build, src, bin, root = build_data()
        self.assertEqual(readme.largest_file(), readme)
        self.assertEqual(src.largest_file(), build)
        self.assertEqual(bin.largest_file(), None)
        self.assertEqual(root.largest_file(), build)

if __name__ == "__main__":
    unittest.main()