# Exercise 2 — Comprehensions
# Practice: use list and dict comprehensions, no manual for loops

products = [
    {"name": "keyboard", "price": 120.0, "in_stock": True},
    {"name": "monitor",  "price": 850.0, "in_stock": False},
    {"name": "mouse",    "price": 45.0,  "in_stock": True},
    {"name": "headset",  "price": 200.0, "in_stock": True},
]

numbers = [3, 10, 15, 22, 31, 48, 50]

students = [
    {"name": "ana", "score": 8.5, "active": True},
    {"name": "bruno", "score": 6.0, "active": False},
    {"name": "carla", "score": 9.0, "active": True},
    {"name": "daniel", "score": 5.5, "active": False},
]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def main():
    # TODO: list of product names in uppercase
    #  TS: const namesUpper = producs.map(p => p.name.toUpperCase())
    names_upper = [product["name"].upper() for product in products]

    # TODO: list of only in-stock products (full dict)
    #  TS: const inStock = products.filter(p => p.in_stock)
    in_stock = [product for product in products if product["in_stock"]]

    # TODO: dict of { name: price } for products under $200
    #  TS: const affordable = products.filter(p => p.price < 200).reduce((acc, p) => ({...acc, [p.name]: p.price}), {})
    affordable = {product["name"]: product["price"] for product in products if product["price"] < 200}

    print(names_upper)
    print(in_stock)
    print(affordable)


main()
