# Typing
# see PEP 483 and PEP 484

# This option is working, but does not bring much benefit (class hierarchy still needed)
# see the test in a separate file test_gift_cont1.py

from enum import Enum
from typing import TypeVar, Union, Tuple, Callable, Any

#
# Base types
#

# Top class types
class ContentData:
    pass

class DecorationData:
    pass

# recursive container type
CONT = TypeVar("CONT", ContentData, Tuple[DecorationData, "CONT"])

# Note : the following 3 lines are not working
# C = TypeVar("C", bound = ContentData)
# D = TypeVar("D", bound = DecorationData)
# U = TypeVar("U", C, Tuple[D, "U"])     # can't use generic in TypeVar

class ContTools:
    #
    @staticmethod    
    def cata(fContents: Callable, fDecoration: Callable, cont: CONT) -> Any:
        if isinstance(cont, ContentData):
            return fContents(cont)
        else:
            deco, subcont = cont
            subres = ContTools.cata(fContents, fDecoration, subcont)
            return fDecoration(deco, subres)


#
# Concrete types
#

# GiftContent : parent class
class GiftContent(ContentData):
    #
    def __init__(self, price: int):
        self.price = price

# Book
class Book(GiftContent):
    #
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price

# Chocolate enum
class ChocolateType(Enum):
    Dark = 1
    Milk = 2
    SeventyPercent = 3

# chocolate
class Chocolate(GiftContent):
    #
    def __init__(self, type: ChocolateType, price: int):
        self.type = type
        self.price = price

# GiftDecoration : parent class
class GiftDecoration(DecorationData):
    pass

# WrappingPaperStyle enum
class WrappingPaperStyle(Enum):
    HappyBirthday = 1
    HappyHolidays = 2
    SolidColor = 3

# WrappedGift class
class Wrapping(GiftDecoration):
    #
    def __init__(self, paper: WrappingPaperStyle):
        self.paper = paper

# BoxedGift class
class Box(GiftDecoration):
    pass

# WithACard class
class WithACard(GiftDecoration):
    #
    def __init__(self, message: str):
        self.message = message



C = TypeVar("C", bound = ContentData)
D = TypeVar("D", bound = DecorationData)

U = Union[
    C,
    Tuple[D, "U"]
]




if __name__ == "__main__":
    print("Hello world !")