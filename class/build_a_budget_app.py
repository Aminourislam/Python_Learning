#build-a-budget-app

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})
    def withdraw(self, amount, description=""):
        self.amount = -amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})
    
def create_spend_chart(categories):
    pass