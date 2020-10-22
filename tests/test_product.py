import unittest

from lib.product import Bought, Component, Made

def build_data():
    label = Bought(name = "label", weight = 1, vendor= "ACME")
    bottle = Bought(name = "bottle", weight = 2, vendor = "ACME")
    formulation = Bought(name = "formulation", weight = 3, vendor = None)
    shampoo = Made(
        name = "shampoo",
        weight = 10,
        components = [
            Component(qty = 1, product = formulation),
            Component(qty = 1, product = bottle),
            Component(qty = 2, product = label)
        ]
    )
    twoPack = Made(
        name = "twoPack",
        weight = 5,
        components = [
            Component(qty = 2, product = shampoo)
        ]
    )
    return label, bottle, formulation, shampoo, twoPack

class TestProduct(unittest.TestCase):
    #
    def test_weight(self):
        label, bottle, formulation, shampoo, twoPack = build_data()
        self.assertEqual(label.total_weight(), 1)
        self.assertEqual(shampoo.total_weight(), 17)
        self.assertEqual(twoPack.total_weight(), 39)
    #
    def test_most_used_vendor(self):
        label, bottle, formulation, shampoo, twoPack = build_data()
        self.assertEqual(label.most_used_vendor(), ("ACME", 1))
        self.assertEqual(formulation.most_used_vendor(), None)
        self.assertEqual(shampoo.most_used_vendor(), ("ACME", 2))
        self.assertEqual(twoPack.most_used_vendor(), ("ACME", 2))