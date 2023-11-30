from User import User
from Ticket import Ticket

class Transaction:
    def __init__(self, seller: User, buyer: User, amount: float, ticket: Ticket):
        self._seller = seller
        self._buyer = buyer
        self._amount = amount
        self._ticket = ticket

    @property
    def seller(self):
        return self._seller

    @property
    def buyer(self):
        return self._buyer

    @property
    def amount(self):
        return self._amount

    @property
    def ticket(self):
        return self._ticket

    @seller.setter
    def seller(self, new_seller):
        self._seller = new_seller

    @buyer.setter
    def buyer(self, new_buyer):
        self._buyer = new_buyer

    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @ticket.setter
    def ticket(self, new_ticket):
        self._ticket = new_ticket

    ## display

    def get_transaction_summary(self):
        return {
            "Transaction ID": id(self),
            "Seller": self.seller.username,
            "Buyer": self.buyer.username,
            "Amount": self.amount,
            "Ticket ID": self.ticket.ticket_id,
            "Event Name": self.ticket.event.name,
            "Status": "Successful" if self.is_successful_purchase() else "Pending"
        }

    ## update

    def update_transaction_amount(self, new_amount):
        self.amount = new_amount
        print("Transaction amount updated.")

    def update_transaction_ticket(self, new_ticket: Ticket):
        print(f"Transaction {self} ticket updated.")
        self.ticket = new_ticket

    ## operation

    def execute_transaction(self):
        if self.buyer.solde >= self.amount:
            self.seller.solde += self.amount
            self.buyer.solde -= self.amount
            self.ticket.owner = self.buyer
            print("Transaction successful.")
        else:
            print("Transaction failed. Insufficient funds.")

    def refund_transaction(self):
        self.seller.solde -= self.amount
        self.buyer.solde += self.amount
        self.ticket.owner = self.seller
        print("Transaction refunded.")

    def transfer_ticket_ownership(self, new_owner: User):
        if self.ticket.availability and self.is_valid_transaction():
            self.ticket.owner = new_owner
            self.buyer.solde -= self.amount
            new_owner.solde += self.amount
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
            combined_amount = self.amount + transaction2.amount
            combined_transaction = Transaction(self.seller, self.buyer, combined_amount, self.ticket)
            print(
                f"Transactions {self} and {transaction2} have been combined into a new transaction: {combined_transaction}.")
            return combined_transaction
        else:
            print(f"Transactions {self} and {transaction2} cannot be combined.")
            return None

    def apply_transaction_fee(self, fee_percentage: float):
        fee_amount = self.amount * (fee_percentage / 100)
        self.amount -= fee_amount
        print(f"A transaction fee of {fee_percentage}% has been applied to Transaction {self}.")
        print(f"New transaction amount: {self.amount} €")

    def reverse_transaction(self):
        self.seller.solde -= self.amount
        self.buyer.solde += self.amount
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
        return self.buyer.solde >= self.amount

    def is_ticket_owned_by_buyer(self):
        return self.ticket.owner == self.buyer

    def check_ticket_validity(self):
        return self.ticket.check_ticket_validity()

    def check_ticket_availability(self):
        return self.ticket.availability

    def check_transaction_balance(self):
        return self.seller.solde >= self.amount

    def check_transaction_participation(self, user: User):
        return user == self.seller or user == self.buyer

    def is_successful_purchase(self):
        return self.ticket.owner == self.buyer

    ### °°° other functions °°°

    ## idée -> appliquer transaction fees
