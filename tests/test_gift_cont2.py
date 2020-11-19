import unittest

from lib.gift_cont2 import RecContainer, Box, CONT, Book, ChocolateType, Chocolate, GiftContents, GiftDecoration, WithACard, Wrapping, WrappingPaperStyle, Box

def build_data():
    wolfHall = Book(title="Wolf Hall", price=2000)
    yummyChoc = Chocolate(ChocolateType.SeventyPercent, 500)
    wrappedWHall = Wrapping(WrappingPaperStyle.HappyBirthday, 50), wolfHall
    birthdayPresent = WithACard("Happy Birthday", 200), wrappedWHall
    boxedYummyChoc = Box(100), yummyChoc
    chistmasPresent = Wrapping(WrappingPaperStyle.HappyHolidays, 50), boxedYummyChoc
    return wolfHall, yummyChoc, wrappedWHall, birthdayPresent, boxedYummyChoc, chistmasPresent

class TestGiftCont(unittest.TestCase):

    def test_totalcost_cata(self):
        wolfHall, yummyChoc, wrappedWHall, birthdayPresent, boxedYummyChoc, chistmasPresent = build_data()
        def fContents(cont):
            return cont.price
        def fDecoration(deco, subprice):
            return deco.price + subprice
        def total_cost(cont: CONT):
            return RecContainer.cata(fContents, fDecoration, cont)
        res0 = total_cost(wolfHall)
        res1 = total_cost(birthdayPresent)
        res2 = total_cost(chistmasPresent)
        self.assertEqual(res0, 2000)
        self.assertEqual(res1, 2250)
        self.assertEqual(res2, 650)