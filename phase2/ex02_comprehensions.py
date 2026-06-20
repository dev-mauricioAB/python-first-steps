# Exercise 2 — Comprehensions
# Practice: use list and dict comprehensions, no manual for loops

products = [
    {"name": "keyboard", "price": 120.0, "in_stock": True},
    {"name": "monitor",  "price": 850.0, "in_stock": False},
    {"name": "mouse",    "price": 45.0,  "in_stock": True},
    {"name": "headset",  "price": 200.0, "in_stock": True},
]


def main():
    # TODO: list of product names in uppercase
    names_upper = []

    # TODO: list of only in-stock products (full dict)
    in_stock = []

    # TODO: dict of { name: price } for products under $200
    affordable = {}

    print(names_upper)
    print(in_stock)
    print(affordable)


main()
