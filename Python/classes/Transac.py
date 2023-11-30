class Transaction:
    def __init__(self, buyer, seller, amount, product):
        self._buyer = buyer
        self._seller = seller
        self._amount = amount
        self._product = product

    ## property / setter

    @property
    def buyer(self):
        return self._buyer

    @property
    def seller(self):
        return self._seller

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    @buyer.setter
    def set_buyer(self, new_buyer):
        self._buyer = new_buyer

    @seller.setter
    def set_seller(self, new_seller):
        self._seller = new_seller

    @amount.setter
    def set_amount(self, new_amount):
        self._amount = new_amount

    @product.setter
    def set_product(self, new_product):
        self._product = new_product

    ### °°° other functions °°°

