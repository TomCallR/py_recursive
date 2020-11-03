import unittest
from lib.linkedlist import LinkedList, Cons, Empty, LList, Union_LList, identity

def build_data():
    nonelist = None
    new123: LinkedList[int] = Cons(1, Cons(2, Cons(3, Empty())))
    return nonelist, new123

class TestLinkedList(unittest.TestCase):
    #
    def test_sum_int_fold(self):
        nonelist, new123 = build_data()
        self.assertEqual(new123.fold(lambda x,y: x+y, lambda x: x, 0), 6)
    #
    def test_sum_int_foldback(self):
        fNode = lambda x,y: x+y
        fLeaf = lambda: 0
        fId = lambda x: x
        nonelist, new123 = build_data()
        self.assertEqual(new123.foldback(fNode, fLeaf, fId), 6)
    #
    def test_convert_to_list_foldback(self):
        fLeaf = lambda: []
        fNode = lambda x,y : [x] + y
        fId = lambda x: x
        nonelist, new123 = build_data()
        self.assertEqual(new123.foldback(fNode, fLeaf, fId), [1, 2, 3])
    #
    def test_map_foldback(self):   
        nonelist, new123 = build_data()
        expected: LinkedList[int] = Cons(11, Cons(12, Cons(13, Empty())))
        self.assertEqual(new123.map_foldback(lambda x: x+10), expected)    
    #
    def test_filter_foldback(self):   
        nonelist, new123 = build_data()
        expected: LinkedList[int] = Cons(1, Cons(3, Empty()))
        self.assertEqual(new123.filter_foldback(lambda x: x%2 == 1), expected)    
    #
    def test_rev_fold(self):   
        nonelist, new123 = build_data()
        actual = new123.rev_fold()
        expected: LinkedList[int] = Cons(3, Cons(2, Cons(1, Empty())))
        self.assertEqual(actual, expected)    


class TestLList(unittest.TestCase):
    #
    def test_tostring_cata(self):
        # pb : the test succeeds, it does not enforce type homogeneity
        list123: LList = (1, (2, ("3", None)))
        expected = "(1, (2, (3, None)))"
        def fCons(value, next):
            return f"({value}, {next})"
        def fEmpty():
            return "None"
        self.assertEqual(Union_LList.cata(fCons, fEmpty, list123), expected)
    #
    def test_sum_int_fold(self):
        list123: LList = (1, (2, (3, None)))
        def fCons(acc, value):
            return acc + value
        def fEmpty(acc):
            return acc
        self.assertEqual(Union_LList.fold(fCons, fEmpty, 0, list123), 6)
    #
    def test_sum_int_foldback(self):
        list123: LList = (1, (2, (3, None)))
        def fCons(value, x):
            return value + x
        def fEmpty():
            return 0
        self.assertEqual(Union_LList.foldback(fCons, fEmpty, list123, identity), 6)
    #
    def test_convert_to_list_foldback(self):
        list123: LList = (1, (2, (3, None)))
        expected = [1, 2, 3]
        def fCons(value, x):
            return [value] + x
        def fEmpty():
            return []
        self.assertEqual(Union_LList.foldback(fCons, fEmpty, list123, identity), expected)
    #
    def test_map_foldback(self):
        list123: LList = (1, (2, (3, None)))
        expected: LList = (11, (12, (13, None)))
        self.assertEqual(Union_LList.map_foldback(list123, lambda x: x+10), expected)
    #
    def test_filter_foldback(self):
        list123: LList = (1, (2, (3, None)))
        expected: LList = (1, (3, None))
        self.assertEqual(Union_LList.filter_foldback(list123, lambda x: x%2 == 1), expected)
    #
    def test_rev_fold(self):   
        list123: LList = (1, (2, (3, None)))
        expected: LList = (3, (2, (1, None)))
        self.assertEqual(Union_LList.rev_fold(list123), expected)