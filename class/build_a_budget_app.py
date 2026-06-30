'''
Build a Budget App

In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

    You should have a Category class that accepts a name as the argument.

    The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.

    The Category class should have the following methods:
        A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
        A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
        A get_balance method that returns the current category balance based on ledger.
        A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
        A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.

    When a Category object is printed, it should:
        Display a title line of 30 characters with the category name centered between * characters.
        List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
        Show a final line Total: [balance], where [balance] should be replaced by the category total.

    Here is an example usage:

    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

    And here is an example of the output:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96

    You should have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string. To build the chart:
        Start with the title Percentage spent by category.
        Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
        Label the y-axis from 100 down to 0 in steps of 10.
        Use o characters for the bars.
        Include a horizontal line two spaces past the last bar.
        Write category names vertically below the bar.

    This function will be tested with up to four categories.

    Make sure to match the spacing of the example output exactly:

    Percentage spent by category
    100|          
     90|          
     80|          
     70|          
     60| o        
     50| o        
     40| o        
     30| o        
     20| o  o     
     10| o  o  o  
      0| o  o  o  
        ----------
         F  C  A  
         o  l  u  
         o  o  t  
         d  t  o  
            h     
            i     
            n     
            g     
'''

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * (30 - len(self.name) - (30 - len(self.name)) // 2)}"
        lines = [title]

        for item in self.ledger:
            desc = item["description"][:23]  # truncate to 23 chars
            amt = f"{item['amount']:.2f}"[:7]  # at most 7 chars (including sign)
            lines.append(f"{desc:<23}{amt:>7}")

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(total)

    total_spent = sum(spent)
    percentages = [int((s / total_spent) * 10) * 10 if total_spent else 0 for s in spent]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for pct in percentages:
            if pct >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"  # trailing space before newline (matches example)

    # Horizontal line: 4 spaces, then dashes for each category (3 dashes per category + 1 extra)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        chart += "     "  # 5 spaces to align under the bars
        for name in names:
            if i < len(name):
                chart += name[i] + "  "  # letter + 2 spaces
            else:
                chart += "   "           # 3 spaces when no letter
        chart += "\n"

    return chart.rstrip("\n")  # remove trailing newline if any