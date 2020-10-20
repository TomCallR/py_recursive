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
    def test_print_description(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        self.assertEqual(wolfHall.__str__(), "\"Wolf Hall\"")
        self.assertEqual(yummyChoc.__str__(), "SeventyPercent chocolate")
        self.assertEqual(
            birthdayPresent.__str__(),
            "\"Wolf Hall\" wrapped in HappyBirthday paper with a card saying \"Happy Birthday\""
            )
        self.assertEqual(
            christmasPresent.__str__(),
            "SeventyPercent chocolate in a box wrapped in HappyHolidays paper"
            )


if __name__ == "__main__":
    unittest.main()