from enum import Enum
from decimal import Decimal as D
from lib.helpers import Convert

# Gift base class
class Gift:
    def __str__(self):
        raise NotImplementedError

# Book class
class Book(Gift):
    #
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = Convert.iprice_to_decimal(price)
    #
    def __str__(self):
        return f"\"{self.title}\""
    #
    def total_cost(self):
        return self.price

# Chocolate enum
class ChocolateType(Enum):
    Dark = 1
    Milk = 2
    SeventyPercent = 3

# Chocolate class
class Chocolate(Gift):
    #
    def __init__(self, type: ChocolateType, price: int):
        self.type = type
        self.price = Convert.iprice_to_decimal(price)
    #
    def __str__(self):
        return f"{self.type.name} chocolate"
    #
    def total_cost(self):
        return self.price

# WrappingPaperStyle enum
class WrappingPaperStyle(Enum):
    HappyBirthday = 1
    HappyHolidays = 2
    SolidColor = 3

# WrappedGift class
class WrappedGift(Gift):
    #
    def __init__(self, gift: Gift, paper: WrappingPaperStyle):
        self.gift = gift
        self.paper = paper
    #
    def __str__(self):
        return f"{self.gift.__str__()} wrapped in {self.paper.name} paper"
    #
    def total_cost(self):
        wrapping_price = D("0.50")
        return self.gift.total_cost() + wrapping_price

# BoxedGift class
class BoxedGift(Gift):
    #
    def __init__(self, gift: Gift):
        self.gift = gift
    #
    def __str__(self):
        return f"{self.gift.__str__()} in a box"
    #
    def total_cost(self):
        box_price = D("1.00")
        return self.gift.total_cost() + box_price

# WithACard class
class WithACard(Gift):
    #
    def __init__(self, gift: Gift, message: str):
        self.gift = gift
        self.message = message
    #
    def __str__(self):
        return f"{self.gift.__str__()} with a card saying \"{self.message}\""
    #
    def total_cost(self):
        card_price = D("2.00")
        return self.gift.total_cost() + card_price

if __name__ == "__main__":
    print("Hello world")

