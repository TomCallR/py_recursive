from enum import Enum

# Gift base class
class Gift:
    pass

# Book class
class Book(Gift):
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price

# Chocolate enum
class ChocolateType(Enum):
    Dark = 1
    Milk = 2
    SeventyPercent = 3

# Chocolate class
class Chocolate(Gift):
    def __init__(self, type: ChocolateType, price: int):
        self.type = ChocolateType
        self.price = price

# WrappingPaperStyle enum
class WrappingPaperStyle(Enum):
    HappyBirthday = 1
    HappyHolidays = 2
    SolidColor = 3

# WrappedGift class
class WrappedGift(Gift):
    def __init__(self, gift: Gift, paper: WrappingPaperStyle):
        self.gift = gift
        self.paper = paper

# BoxedGift class
class BoxedGift(Gift):
    def __init__(self, gift: Gift):
        self.gift = gift

# WithACard class
class WithACard(Gift):
    def __init__(self, gift: Gift, message: str):
        self.gift = gift
        self.message = message

# if __name__ == "__main__":
#     print("Hello world")

