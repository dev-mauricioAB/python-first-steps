# Exercise 4 — File I/O + Data Reshaping
# Practice: read JSON, reshape data with comprehension, write result to new file
#
# Expected input file: orders.json (create it if it doesn't exist)
# [
#   { "id": 1, "customer": "Alice", "total": 320.0, "status": "delivered" },
#   { "id": 2, "customer": "Bob",   "total": 85.5,  "status": "pending"   },
#   { "id": 3, "customer": "Carol", "total": 540.0, "status": "delivered" },
#   { "id": 4, "customer": "Dan",   "total": 30.0,  "status": "cancelled" }
# ]

import json


def main():
    # TODO: read orders.json

    # TODO: filter only "delivered" orders and add 10% tax
    # result shape: [{ "customer": ..., "total_with_tax": ... }]

    # TODO: write result to orders_summary.json with indent=2

    print("done — check orders_summary.json")


main()
