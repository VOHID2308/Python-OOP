class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} hisobida: {self.balance} som bor.")

    def get_balance(self):
        return self.balance

account1 = BankAccount("Ali", 150_000)
account2 = BankAccount("Nilufar", 200_000)
account3 = BankAccount("Vali", 75_000)
account4 = BankAccount("Lola", 125_000)
account5 = BankAccount("Javohir", 100_000)

accounts = [account1, account2, account3, account4, account5]

total_balance = 0
for account in accounts:
    total_balance += account.get_balance()

print(f"total: {total_balance} som")