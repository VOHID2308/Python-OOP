class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")
        else:
            print(f"{self.name} hozirda tugagan ❌")

product3 = Product("Galaxy Buds", 149.99, "electronics", True)
product4 = Product("MacBook Air", 1299.99, "electronics", False)
product3.check_stock()
product4.check_stock()