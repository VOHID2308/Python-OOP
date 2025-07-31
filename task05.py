class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("AirPods", 199.99, "electronics", True)
product2 = Product("iPhone 13", 999.99, "electronics", False)
print(product1.name, product1.price)
print(product2.name, product2.price)