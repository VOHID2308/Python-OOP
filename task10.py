class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Xatolik: yetarli mablag yoq.")

account1 = BankAccount("Aziz", 1000)
account1.deposit(250)
account1.withdraw(500)
account1.withdraw(800)