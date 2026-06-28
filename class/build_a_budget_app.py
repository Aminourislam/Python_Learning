class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self, amount, description=""):
        if check_funds(amount):
            self.amount = -amount
            self.description = description
            self.ledger.append({'amount': self.amount, 'description': self.description})
            return True
        else:
            return False


    def get_balance(self):
        balance = 0
        for transection in ledger:
            balance += transection["amount"]
        return balance

    def transfer(self, amount, destination):
        self.amount = amount
        if check_funds(self.amount):            
            self.destination = f"Transfer to [{destination}]"
            self.withdraw(self.amount, self.destination)
            destination.deposit(self.amount, f"Transfer from [{self.name}]")
            return True
        else:
            return False

    def check_funds(self, amount):
        self.amount = amount
        self.balance = get_balance()
        if self.balance >= self.amount:
            return True
        else:
            return False
        

def create_spend_chart(categories):
    def __init__(self, ):
        self.title = ""



'''
NOTE: open the browser console with F12 to see a more verbose output of the tests.
Tests:

Waiting: 1. The deposit method should create a specific object in the ledger instance variable.
Waiting: 2. Calling the deposit method with no description should create a blank description.
Waiting: 3. The withdraw method should create a specific object in the ledger instance variable.
Waiting: 4. Calling the withdraw method with no description should create a blank description.
Waiting: 5. The withdraw method should return True if the withdrawal took place.
Waiting: 6. Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33.
Waiting: 7. Calling the transfer method on a category object should create a specific ledger item in that category object.
Waiting: 8. The transfer method should return True if the transfer took place.
Waiting: 9. Calling transfer on a category object should reduce the balance in the category object.
Waiting: 10. The transfer method should increase the balance of the category object passed as its argument.
Waiting: 11. The transfer method should create a specific ledger item in the category object passed as its argument.
Waiting: 12. The check_funds method should return False if the amount passed to the method is greater than the category balance.
Waiting: 13. The check_funds method should return True if the amount passed to the method is not greater than the category balance.
Waiting: 14. The withdraw method should return False if the withdrawal didn't take place.
Waiting: 15. The transfer method should return False if the transfer didn't take place.
Waiting: 16. Printing a Category instance should give a different string representation of the object.
Waiting: 17. Title at the top of create_spend_chart chart should say Percentage spent by category.
Waiting: 18. create_spend_chart chart should have correct percentages down the left side.
Waiting: 19. The height of each bar on the create_spend_chart chart should be rounded down to the nearest 10.
Waiting: 20. Each line in create_spend_chart chart should have the same length. Bars for different categories should be separated by two spaces, with additional two spaces after the final bar.
Waiting: 21. create_spend_chart should correctly show horizontal line below the bars. Using three - characters for each category, and in total going two characters past the final bar.
Waiting: 22. create_spend_chart chart should not have new line character at the end.
Waiting: 23. create_spend_chart chart should have each category name written vertically below the bar. Each line should have the same length, each category should be separated by two spaces, with additional two spaces after the final category.
Waiting: 24. create_spend_chart should print a different chart representation. Check that all spacing is exact. Open your browser console with F12 for more details.
'''