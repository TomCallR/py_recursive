from decimal import Decimal as D

class Convert:
    # @classmethod
    # def int_to_amount(cls, val: int):
    #     r = val % 100
    #     q = val // 100
    #     return f"{q},{r}"
    
    @classmethod
    def iprice_to_decimal(cls, val: int):
        return (D(val) * D("1.00")).shift(-2)
