# Making gift abstract
from typing import TypeVar, Union, Tuple, Callable, Callable, Any
from abc import ABC
from enum import Enum

#
# Abstract constructs
#
class ContentData(ABC):
    pass

class DecorationData(ABC):
    pass

# recursive container type
CONT = Union[ContentData, Tuple[DecorationData, "CONT"]]

class RecContainer:
    #
    @staticmethod
    def cata(
        fContents: Callable[[ContentData], Any],
        fDecoration: Callable[[DecorationData, CONT], Any],
        value: CONT
        ) -> Any:
        if isinstance(value, ContentData):
            return fContents(value)
        else:
            decoration, subcont = value
            return fDecoration(decoration, RecContainer.cata(fContents, fDecoration, subcont))
    #
    @staticmethod
    def fold(
        fContents: Callable[[Any, ContentData], Any],
        fDecoration: Callable[[Any, DecorationData], Any],
        acc: Any,
        value: CONT
        ) -> Any:
        if isinstance(value, ContentData):
            return fContents(acc, value)
        else:
            decoration, subcont = value
            newacc = fDecoration(acc, decoration)
            return RecContainer.fold(fContents, fDecoration, newacc, subcont)


#
# Concrete elements
#
class GiftContents(ContentData):
    def __init__(self, price: int):
        self.price = price

class GiftDecoration(DecorationData):
    def __init__(self, price: int):
        self.price = price

# Book
class Book(GiftContents):
    #
    def __init__(self, title: str, price: int):
        self.title = title
        super().__init__(price)

# Chocolate enum
class ChocolateType(Enum):
    Dark = 1
    Milk = 2
    SeventyPercent = 3

# chocolate
class Chocolate(GiftContents):
    #
    def __init__(self, type: ChocolateType, price: int):
        self.type = type
        super().__init__(price)

# WrappingPaperStyle enum
class WrappingPaperStyle(Enum):
    HappyBirthday = 1
    HappyHolidays = 2
    SolidColor = 3

# WrappedGift class
class Wrapping(GiftDecoration):
    #
    def __init__(self, paper: WrappingPaperStyle, price: int):
        self.paper = paper
        super().__init__(price)

# BoxedGift class
class Box(GiftDecoration):
    #
    def __init__(self, price: int):
        super().__init__(price)

# WithACard class
class WithACard(GiftDecoration):
    #
    def __init__(self, message: str, price: int):
        self.message = message
        super().__init__(price)
        
