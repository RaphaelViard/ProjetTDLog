class Transaction:
    def __init__(self, seller, buyer, price, ticket):
        self._seller = seller
        self._buyer = buyer
        self._price = price
        self._ticket = ticket

    @property
    def seller(self):
        return self._seller

    @property
    def buyer(self):
        return self._buyer

    @property
    def price(self):
        return self._price

    @property
    def ticket(self):
        return self._ticket

    @seller.setter
    def seller(self, new_seller):
        self._seller = new_seller

    @buyer.setter
    def buyer(self, new_buyer):
        self._buyer = new_buyer

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @ticket.setter
    def ticket(self, new_ticket):
        self._ticket = new_ticket

    ## display

    def get_transaction_summary(self):
        return {
            "Transaction ID": id(self),
            "Seller": self.seller.username,
            "Buyer": self.buyer.username,
            "Seller": self.seller._username,
            "Buyer": self.buyer._username,
            "Amount": self.price,
            "Ticket ID": self.ticket.id,
            "Event Name": self.ticket.event.name,
            "Status": "Successful" if self.is_successful_purchase() else "Pending"
        }

    ## update

    def update_transaction_amount(self, new_price):
        self.price = new_price
        print("Transaction amount updated.")

    def update_transaction_ticket(self, new_ticket):
        print(f"Transaction {self} ticket updated.")
        self.ticket = new_ticket

    ## operation

    def execute_transaction(self):
        if self.buyer.solde >= self.price:
            self.seller.solde += self.price
            self.buyer.solde -= self.price
        if self.buyer._solde >= self.price:
            self.seller._solde += self.price
            self.buyer._solde -= self.price
            self.ticket.owner = self.buyer
            print("Transaction successful.")
        else:
            print("Transaction failed. Insufficient funds.")

    def refund_transaction(self):
        self.seller.solde -= self.price
        self.buyer.solde += self.price
        self.ticket.owner = self.seller
        print("Transaction refunded.")

    def transfer_ticket_ownership(self, new_owner):
        if self.ticket.availability and self.is_valid_transaction():
            self.ticket.owner = new_owner
            self.buyer.solde -= self.price
            new_owner.solde += self.price
            print(f"Ticket ownership transferred to {new_owner.username}.")
        else:
            print("Ticket transfer failed. Either the ticket is not available or the transaction is invalid.")

    def split_transaction(self, new_amount1: float, new_amount2: float):
        if self.is_valid_transaction():
            transaction1 = Transaction(self.seller, self.buyer, new_amount1, self.ticket)
            transaction2 = Transaction(self.seller, self.buyer, new_amount2, self.ticket)
            print(f"Transaction {self} has been split into two new transactions: {transaction1} and {transaction2}.")
            return transaction1, transaction2
        else:
            print(f"Transaction {self} cannot be split as it is not valid.")
            return None, None

    def combine_transactions(self, transaction2):
        if self.is_valid_transaction() and transaction2.is_valid_transaction():
            combined_amount = self.price + transaction2.price
            combined_transaction = Transaction(self.seller, self.buyer, combined_amount, self.ticket)
            print(
                f"Transactions {self} and {transaction2} have been combined into a new transaction: {combined_transaction}.")
            return combined_transaction
        else:
            print(f"Transactions {self} and {transaction2} cannot be combined.")
            return None

    def apply_transaction_fee(self, fee_percentage: float):
        fee_amount = self.price * (fee_percentage / 100)
        self.price -= fee_amount
        print(f"A transaction fee of {fee_percentage}% has been applied to Transaction {self}.")
        print(f"New transaction amount: {self.price} €")

    def reverse_transaction(self):
        self.seller.solde -= self.price
        self.buyer.solde += self.price
        self.ticket.owner = self.seller
        print("Transaction reversed.")

    def mark_transaction_as_successful(self):
        print(f"Transaction {self} marked as successful.")
        self.seller.add_purchase_history(self)
        self.buyer.add_purchase_history(self)

    def mark_transaction_as_pending(self):
        print(f"Transaction {self} marked as pending.")
        self.seller.remove_purchase_history(self)
        self.buyer.remove_purchase_history(self)

    ## verification

    def is_valid_transaction(self):
        return self.buyer.solde >= self.price

    def is_ticket_owned_by_buyer(self):
        return self.ticket.owner == self.buyer

    def check_ticket_validity(self):
        return self.ticket.check_ticket_validity()

    def check_ticket_availability(self):
        return self.ticket.availability

    def check_transaction_balance(self):
        return self.seller.solde >= self.price

    def check_transaction_participation(self, user):
        return user == self.seller or user == self.buyer

    def is_successful_purchase(self):
        return self.ticket.owner == self.buyer

    ### °°° other functions °°°

