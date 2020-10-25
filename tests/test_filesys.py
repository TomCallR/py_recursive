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
    def test_totalsize_cata(self):
        readme, config, build, src, bin, root = build_data()
        self.assertEqual(readme.total_size_cata(), 1)
        self.assertEqual(src.total_size_cata(), 16)
        self.assertEqual(root.total_size_cata(), 31)
    #
    def test_largestfile_cata(self):
        readme, config, build, src, bin, root = build_data()
        self.assertEqual(readme.largest_file_cata(), readme)
        self.assertEqual(src.largest_file_cata(), build)
        self.assertEqual(bin.largest_file_cata(), None)
        self.assertEqual(root.largest_file_cata(), build)
    #
    def test_totalsize_fold(self):
        readme, config, build, src, bin, root = build_data()
        self.assertEqual(readme.total_size_fold(), 1)
        self.assertEqual(src.total_size_fold(), 16)
        self.assertEqual(root.total_size_fold(), 31)
    #
    def test_largestfile_fold(self):
        readme, config, build, src, bin, root = build_data()
        self.assertEqual(readme.largest_file_fold(), readme)
        self.assertEqual(src.largest_file_fold(), build)
        self.assertEqual(bin.largest_file_fold(), None)
        self.assertEqual(root.largest_file_fold(), build)


if __name__ == "__main__":
    unittest.main()