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
    pass