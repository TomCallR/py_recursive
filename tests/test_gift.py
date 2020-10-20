import builtins
import unittest

# import lib
import lib.gift
from lib.gift import Gift, Book, ChocolateType, Chocolate, WithACard, WrappedGift, WrappingPaperStyle, BoxedGift

def build_data():    
    wolfHall = Book(title="Wolf Hall", price=20)
    yummyChoc = Chocolate(
        type=ChocolateType.SeventyPercent,
        price = 5)
    birthdayPresent = WithACard(
        gift = WrappedGift(gift = wolfHall, paper = WrappingPaperStyle.HappyBirthday),
        message = "Happy Birthday")
    christmasPresent = WrappedGift(
        gift = BoxedGift(gift = yummyChoc),
        paper = WrappingPaperStyle.HappyHolidays)
    return wolfHall, yummyChoc, birthdayPresent, christmasPresent

class TestGiftDeclaration(unittest.TestCase):

    #
    def test_basic_print_attributes(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        print(f"{wolfHall.title} - {wolfHall.price}")
        print(f"{yummyChoc.type} - {yummyChoc.price}")
        print(f"{birthdayPresent.gift} - {birthdayPresent.message}")
        print(f"{christmasPresent.gift} - {christmasPresent.paper}")

if __name__ == "__main__":
    unittest.main()