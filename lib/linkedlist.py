# Note : Linked list implementation does not have much interest beyond training
# Python already has a collection type that is a linked list : deque
from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    """
        Singly linked list of elements of the same type
        The checks performed by __init__() are meant to avoid different types
        in the list nodes
    """
    def __init__(self, head: T, tail):
        if head is None:
            raise TypeError
        if tail is not None:
            try:
                tail_head = tail.head
            except Exception as ex:
                raise TypeError
            if type(tail_head) != type(head):
                raise TypeError
        self.tail = tail
        self.head = head
    #
    def cata(self, fNode):
        if self.tail is None:
            return fNode(self.head, None)
        else:
            return fNode(self.head, self.tail.cata(fNode))
    #
    def fold(self, fNode, acc):
        newacc = fNode(acc, self.head)
        if self.tail is None:
            return newacc
        else:
            return self.tail.fold(fNode, newacc)
    #
    def foldback(self, fNode, fLeaf, facc):
        if self.tail is None:
            return facc(fLeaf(self.head))
        else:
            def innerfacc(x, head: T):
                return facc(fNode(head, x))
            newfacc = lambda x: innerfacc(x, self.head)
            return self.tail.foldback(fNode, fLeaf, newfacc)


#
if __name__ == "__main__":
    print("Hello world")
