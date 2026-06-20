# Exercise 5 — Utility Script (Putting It Together)
# Practice: typed functions, comprehensions, exceptions, file I/O — all in one

import json


def load_orders(path: str) -> list[dict]:
    # TODO: read and return JSON from path
    # raise FileNotFoundError with a clear message if the file doesn't exist
    pass


def summarize_orders(orders: list[dict]) -> dict:
    # TODO: return a summary dict using comprehensions where possible
    # shape:
    # {
    #     "total_orders": int,
    #     "delivered": int,
    #     "pending": int,
    #     "cancelled": int,
    #     "revenue": float  — sum of delivered orders only
    # }
    pass


def main():
    try:
        orders = load_orders("orders.json")
        summary = summarize_orders(orders)

        # TODO: print each key/value in a readable format
        # example:
        # total_orders : 4
        # delivered    : 2
        # revenue      : 860.0

    except FileNotFoundError as e:
        print(f"Error: {e}")


main()
