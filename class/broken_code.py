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
        # Title line: 30 chars with name centered between *
        title = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * (30 - len(self.name) - (30 - len(self.name)) // 2)}"
        # Ledger entries
        lines = [title]
        for item in self.ledger:
            desc = item["description"][:23]  # truncate to 23 chars
            amt = f"{item['amount']:.2f}"[:7]  # at most 7 chars (including sign)
            lines.append(f"{desc:<23}{amt:>7}")
        # Total
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    # Calculate total spent (withdrawals) per category
    spent = []
    for cat in categories:
        total = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(total)

    total_spent = sum(spent)
    # Percentages rounded down to nearest 10
    percentages = [int((s / total_spent) * 10) * 10 if total_spent else 0 for s in spent]

    chart = "Percentage spent by category\n"

    # Y‑axis from 100 down to 0
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