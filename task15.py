class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

product1 = Product("milk", 10_000, True)
product2 = Product("qurut", 12_000, False)
product3 = Product("coke", 8_000, True)
product4 = Product("fuse tea", 3_000, True)
product5 = Product("cake", 9_500, False)

products = [product1, product2, product3, product4, product5]

total = 0
for product in products:
    if product.in_stock:
        total += product.price

print(f"the price of product: {total} som")