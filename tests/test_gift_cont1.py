import unittest

from lib import gift_cont1

def build_data():
    wolfHall = gift_cont1.Book(title="Wolf Hall", price=2000)
    yummyChoc = gift_cont1.Chocolate(
        type = gift_cont1.ChocolateType.SeventyPercent,
        price = 500)
    wrappedWHall = (gift_cont1.Wrapping(gift_cont1.WrappingPaperStyle.HappyBirthday), wolfHall)
    birthdayPresent = (gift_cont1.WithACard(message = "Happy Birthday"), wrappedWHall)
    boxedYummyChoc = (gift_cont1.Box(), yummyChoc)
    chistmasPresent = (gift_cont1.Wrapping(gift_cont1.WrappingPaperStyle.HappyHolidays), boxedYummyChoc)
    return wolfHall, yummyChoc, wrappedWHall, birthdayPresent, boxedYummyChoc, chistmasPresent

class TestGiftCont(unittest.TestCase):

    def test_totalcost_cata(self):
        wolfHall, yummyChoc, wrappedWHall, birthdayPresent, boxedYummyChoc, chistmasPresent = build_data()
        def fContents(cont: gift_cont1.CONT):
            return cont.price
        def fDecoration(deco, subprice):
            if isinstance(deco, gift_cont1.Wrapping):
                return 50 + subprice
            elif isinstance(deco, gift_cont1.Box):
                return 100 + subprice
            else:
                return 200 + subprice
        def total_cost(cont: gift_cont1.CONT):
            return gift_cont1.ContTools.cata(fContents, fDecoration, cont)
        res0 = total_cost(wolfHall)
        res1 = total_cost(birthdayPresent)
        res2 = total_cost(chistmasPresent)
        self.assertEqual(res0, 2000)
        self.assertEqual(res1, 2250)
        self.assertEqual(res2, 650)