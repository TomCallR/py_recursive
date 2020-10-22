from typing import List, Tuple
import functools

class Product:
    #
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    #
    def total_weight(self):
        def fBought(item: Product):
            return item.weight
        def fMade(name: str, weight: int, comptup: List[Tuple[int, int]]):
            compweights = [q * w for (q, w) in comptup]
            return weight + sum(compweights)
        return self.cata(fBought, fMade)
    #
    def most_used_vendor(self):
        def compare_scores(acc, new):
            if acc is None:
                return new
            elif new is None:
                return acc
            elif new[1] > acc[1]:
                return new
            else:
                return acc
        def fBought(item: Product):
            # beware: vendor can be None
            if item.vendor is None:
                return None
            else:
                return (item.vendor, 1)  
        def fMade(name: str, weight: int, comptup: List[Tuple[int, Tuple[str, int]]]):
            # build List[(vendor, n)]
            unit_vendors = [vscore for (qty, vscore) in comptup if vscore is not None]  
            # sum per vendor using a dict
            vendor_scores = {v: 0 for v, n in unit_vendors}
            for v, n in unit_vendors:
                vendor_scores[v] += n
            # get the vendor with highest score
            vendor_scores = zip(vendor_scores.keys(), vendor_scores.values())
            res = functools.reduce(compare_scores, vendor_scores, None)
            return res
        return self.cata(fBought, fMade)


class Bought(Product):
    #
    def __init__(self, name: str, weight: int, vendor: str):
        super().__init__(name, weight)
        self.vendor = vendor
    #
    def cata(self, fBought, fMade):
        return fBought(self)

class Component:
    #
    def __init__(self, qty: int, product: Product):
        self.qty = qty
        self.product = product
    #
    def cata(self, fBought, fMade):
        return self.qty, self.product.cata(fBought, fMade)

class Made(Product):
    #
    def __init__(self, name: str, weight: int, components: List[Component]):
        super().__init__(name, weight)
        self.components = components
    #
    def cata(self, fBought, fMade):
        comptup = [item.cata(fBought, fMade) for item in self.components]
        return fMade(self.name, self.weight, comptup)