from typing import List

class Product:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class Bought(Product):
    #
    def __init__(self, name: str, weight: int, vendor: str):
        super().__init__(name, weight)
        self.vendor = vendor
    #
    def cata(self, fBought, fMade, fComponent):
        return fBought(self)

class Component:
    #
    def __init__(self, qty: int, component: Product):
        self.qty = qty
        self.component = component
    #
    def cata(self, fBought, fMade, fComponent):
        return fComponent(self)

class Made(Product):
    #
    def __init__(self, name: str, weight: int, components: List[Component]):
        super().__init__(name, weight)
        self.components = components
    #
    def cata(self, fBought, fMade, fComponent):
        compres = [item.cata(fBought, fMade, fComponent) for item in self.components]
        return fComponent(self.name, self.weight, compres)