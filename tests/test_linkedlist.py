import unittest
from lib.linkedlist import Node

def build_data():
    nonelist = None
    one23 = Node[int](1, Node[int](2, Node[int](3, None)))
    return nonelist, one23

class TestLinkedList(unittest.TestCase):
    #
    def test_sum_int_fold(self):
        nonelist, one23 = build_data()
        self.assertEqual(one23.fold(lambda x,y: x+y, 0), 6)
    #
    def test_sum_int_foldback(self):
        fNode = lambda x,y: x+y
        fLeaf = lambda x: x
        fId = fLeaf
        nonelist, one23 = build_data()
        self.assertEqual(one23.foldback(fNode, fLeaf, fId), 6)
    #
    def test_convert_to_list_foldback(self):
        fLeaf = lambda x: [x]
        fNode = lambda x,y : [x] + y
        fId = lambda x: x
        nonelist, one23 = build_data()
        self.assertEqual(one23.foldback(fNode, fLeaf, fId), [1, 2, 3])
    