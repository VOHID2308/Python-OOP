class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} - {self.price} som")


product1 = Product("iPhone 13", 12_000_000, "Electronics")
product2 = Product("Camera", 9_500_000, "Photography")

products = [product1, product2]

most_expensive = products[0]
for product in products[1:]:
    if product.price > most_expensive.price:
        most_expensive = product

print("the most expensive one:")
most_expensive.info()