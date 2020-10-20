import unittest

from decimal import Decimal as D
from lib.helpers import Convert

class TestConvertHelpers(unittest.TestCase):
    #
    # def test_int_to_amount(self):
    #     self.assertEqual(Convert.int_to_amount(12732), "127,32")
    
    def test_iprice_to_decimal(self):
        self.assertEqual(Convert.iprice_to_decimal(12732), D("127.32"))