class BankAccaount:
    def __init__(self, owner) -> None:
        self.owner:str = owner
        self.balance: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
    def show_balance(self) -> None:
        print(f"{self.owner}: Balance ${self.balance:,.2f}")

ba = BankAccaount("Ali")
ba.deposit(100_000)
ba.withdraw(35_000)
ba.show_balance()