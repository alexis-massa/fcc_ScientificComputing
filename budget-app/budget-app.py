class Category:
    """
    A budget Category class for managing deposits, withdrawals, transfers, and balances.
    """
    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description: str = "") -> None:
        """Add a deposit entry to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """Add a withdrawal entry to the ledger if sufficient funds exist."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        """Return the current balance of the category."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, category: 'Category') -> bool:
        """Transfer an amount to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        """Check if the funds are sufficient for the transaction."""
        return amount <= self.get_balance()

    def __str__(self) -> str:
        """Return a formatted string representation of the category ledger."""
        title = self.name.center(30, '*')
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}{total}"


def create_spend_chart(categories: list[Category]) -> str:
    """
    Create a bar chart showing the percentage of spending by category.

    Args:
        categories (list[Category]): A list of Category objects.

    Returns:
        str: A formatted bar chart as a string.
    """
    # Calculate total and percentages
    total_spent = sum(-item['amount'] for cat in categories for item in cat.ledger if item['amount'] < 0)
    category_spent = [sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    percentages = [int(spent / total_spent * 100 // 10) * 10 if total_spent > 0 else 0 for spent in category_spent]

    # Build chart header
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| " + "  ".join("o" if percent >= i else " " for percent in percentages) + "  \n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Build category labels vertically
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    for i in range(max_len):
        chart += "     " + "  ".join(name[i] for name in names) + "  \n"

    return chart.rstrip('\n')


# Example Usage
food = Category('Food')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'Groceries')
food.withdraw(15.89, 'Restaurant')

clothing = Category('Clothing')
clothing.deposit(500, 'Initial deposit')
clothing.withdraw(50.55, 'Jeans')

entertainment = Category('Entertainment')
entertainment.deposit(300, 'Initial deposit')
entertainment.withdraw(75.25, 'Movies')

print(food)
print(clothing)
print(entertainment)
print(create_spend_chart([food, clothing, entertainment]))
