import unittest

from decimal import Decimal as D
from lib.gift import Book, ChocolateType, Chocolate, WithACard, WrappedGift, WrappingPaperStyle, BoxedGift

def build_data():    
    wolfHall = Book(title="Wolf Hall", price=2000)
    yummyChoc = Chocolate(
        type=ChocolateType.SeventyPercent,
        price = 500)
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

    # Fails on purpose : fold mixes the order of elements
    # def test_description_fold(self):
    #     wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
    #     self.assertEqual(wolfHall.description_fold(), "\"Wolf Hall\"")
    #     self.assertEqual(yummyChoc.description_fold(), "SeventyPercent chocolate")
    #     self.assertEqual(
    #         birthdayPresent.description_fold(),
    #         "\"Wolf Hall\" wrapped in HappyBirthday paper with a card saying \"Happy Birthday\""
    #     )
    #     self.assertEqual(
    #         christmasPresent.description_fold(),
    #         "SeventyPercent chocolate in a box wrapped in HappyHolidays paper"
    #     )

    #
    def test_print_description_fold_back(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        self.assertEqual(wolfHall.description_fold_back(), "\"Wolf Hall\"")
        self.assertEqual(yummyChoc.description_fold_back(), "SeventyPercent chocolate")
        self.assertEqual(
            birthdayPresent.description_fold_back(),
            "\"Wolf Hall\" wrapped in HappyBirthday paper with a card saying \"Happy Birthday\""
        )
        self.assertEqual(
            christmasPresent.description_fold_back(),
            "SeventyPercent chocolate in a box wrapped in HappyHolidays paper"
        )

    #
    def test_print_description_foldback(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        self.assertEqual(wolfHall.description_foldback(), "\"Wolf Hall\"")
        self.assertEqual(yummyChoc.description_foldback(), "SeventyPercent chocolate")
        self.assertEqual(
            birthdayPresent.description_foldback(),
            "\"Wolf Hall\" wrapped in HappyBirthday paper with a card saying \"Happy Birthday\""
        )
        self.assertEqual(
            christmasPresent.description_foldback(),
            "SeventyPercent chocolate in a box wrapped in HappyHolidays paper"
        )

    #
    def test_total_cost(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        self.assertEqual(birthdayPresent.total_cost(), D("22.5"))
        self.assertEqual(christmasPresent.total_cost(), D("6.5"))

    #
    def test_total_cost_fold(self):
        wolfHall, yummyChoc, birthdayPresent, christmasPresent = build_data()
        self.assertEqual(birthdayPresent.total_cost_fold(), D("22.5"))
        self.assertEqual(christmasPresent.total_cost_fold(), D("6.5"))


if __name__ == "__main__":
    unittest.main()