# Note : Linked list implementation does not have much interest beyond training
# Python already has a collection type that is a linked list : deque
from typing import TypeVar, Generic, Callable, Union, Tuple, Any

T = TypeVar("T")

def identity(x: Any):
    return x


#
#
# First implementation using a class and two subclasses
#
#
class LinkedList(Generic[T]):
    """
        Singly linked list of elements of the same type
        LinkedList class is the base class for Cons and Empty classes
        
        :Example:

        mylist: LinkedList[int] = Cons(1, Cons(2, Cons(3, Empty())))
    """
    def __init__(self):
        self.value = None
    #
    def cata(self, fCons, fEmpty):
        pass
    #
    def fold(self, fCons, fEmpty, acc):
        pass
    #
    def foldback(self, fCons, fEmpty, facc):
        pass

class Empty(LinkedList[T]):
    #
    def __init__(self):
        super().__init__()
    #
    def __eq__(self, other: Any):
        return isinstance(other, Empty)
    #
    def cata(self, fCons, fEmpty):
        return fEmpty()
    #
    def fold(self, fCons, fEmpty, acc):
        return fEmpty(acc)
    #
    def foldback(self, fCons, fEmpty, facc):
        return facc(fEmpty())
    #
    def map_foldback(self, f: Callable[[T], Any]):
        return Empty()
    #
    def filter_foldback(self, predicate: Callable[[T], bool]):
        return Empty()
    #
    def rev_fold(self):
        return Empty()

class Cons(LinkedList[T]):
    #
    def __init__(self, value: T, next: LinkedList[T]):
        self.value = value
        self.next = next
    # deep nested equality, necessary for tests
    def __eq__(self, other: Any):
        if isinstance(other, Cons):
            equal_values = self.value.__eq__(other.value)
            return equal_values and self.next.__eq__(other.next)        
        else:
            return False
    #
    def cata(self, fCons, fEmpty):
        return fCons(self.value, self.next.cata(fCons, fEmpty))
    #
    def fold(self, fCons, fEmpty, acc: Any):
        newacc = fCons(acc, self.value)
        return self.next.fold(fCons, fEmpty, newacc)
    #
    def foldback(self, fCons, fEmpty, facc):
        def innerfunc(value, x):
            return facc(fCons(value, x))
        newfacc = lambda x: innerfunc(self.value, x)
        return self.next.foldback(fCons, fEmpty, newfacc)
    #
    def map_foldback(self, f: Callable[[T], Any]):
        def fCons(value, following_values):
            return Cons(f(value), following_values)
        def fEmpty():
            return Empty()
        return self.foldback(fCons, fEmpty, identity)
    #
    def filter_foldback(self, predicate: Callable[[T], bool]):
        def fCons(value, following_items):
            if predicate(value):
                return Cons(value, following_items)
            else:
                return following_items
        def fEmpty():
            return Empty()
        return self.foldback(fCons, fEmpty, identity)     
    #
    def rev_fold(self):
        def fCons(acc, value):
            return Cons(value, acc)
        def fEmpty(acc):
            return acc
        return self.fold(fCons, fEmpty, Empty())


#
#
# Second implementation using a union
#
#
# https://devblogs.microsoft.com/python/pylance-introduces-five-new-features-that-enable-type-magic-for-python-developers/
LList = Union[
    None,
    Tuple[T, "LList"]
]

class Union_LList(Generic[T]):
    #
    @staticmethod
    def cata(fCons, fEmpty, llist: LList):
        if llist is None:
            return fEmpty()
        else:
            value, next = llist
            return fCons(value, Union_LList.cata(fCons, fEmpty, next))
    #
    @staticmethod
    def fold(fCons, fEmpty, acc, llist: LList):
        if llist is None:
            return fEmpty(acc)
        else:
            value, next = llist
            newacc = fCons(acc, value)
            return Union_LList.fold(fCons, fEmpty, newacc, next)
    #
    @staticmethod
    def foldback(fCons, fEmpty, llist: LList, facc):
        if llist is None:
            return facc(fEmpty())
        else:
            value, next = llist
            newfacc = lambda x: facc(fCons(value, x))
            return Union_LList.foldback(fCons, fEmpty, next, newfacc)
    #
    @staticmethod
    def map_foldback(llist: LList, f: Callable[[T], Any]):
        def fEmpty():
            return None
        def fCons(value: T, x):
            return (f(value), x)
        return Union_LList.foldback(fCons, fEmpty, llist, identity)
    #
    @staticmethod
    def filter_foldback(llist: LList, predicate: Callable[[T], bool]):
        def fEmpty():
            return None
        def fCons(value: T, x):
            if predicate(value):
                return (value, x)
            else:
                return x
        return Union_LList.foldback(fCons, fEmpty, llist, identity)
    #
    @staticmethod
    def rev_fold(llist: LList):
        def fEmpty(acc):
            return acc
        def fCons(acc, value: T):
            return (value, acc)
        return Union_LList.fold(fCons, fEmpty, None, llist)

#
#
# Third implementation using module ADT
# See https://pypi.org/project/algebraic-data-types/
#
#   TODO


#
if __name__ == "__main__":
    print("Hello world")
