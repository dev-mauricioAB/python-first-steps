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
    _ = json

    # TODO 1: create a fallback list if orders.json doesn't exist or is invalid JSON
    fallback_orders = [
        {"id": 1, "customer": "Alice", "total": 320.0, "status": "delivered"},
        {"id": 2, "customer": "Bob",   "total": 85.5,  "status": "pending"},
        {"id": 3, "customer": "Carol", "total": 540.0, "status": "delivered"},
        {"id": 4, "customer": "Dan",   "total": 30.0,  "status": "cancelled"}
    ]

    # TODO: read orders.json
    try:
        with open("orders.json", "r") as f:
            orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        orders = fallback_orders
    
    # TODO 2: build dict with count of orders by status
    # expected shape: {"delivered": 2, "pending": 1, "cancelled": 1}
    # TS:
    # const statusCounts = orders.reduce((acc, order) => {
    #   const status = order.status;
    #   acc[status] = (acc[status] || 0) + 1;
    #   return acc;
    # }, {});
    status_counts = {
        status: sum(1 for order in orders if order["status"] == status)
        for status in set(order["status"] for order in orders)
    }
    print(status_counts)

    # TODO 3: list customers with total >= 100 (from all orders)
    #  TS: const highValueCustomers = orders.filter(o => o.total >= 100).map(o => o.customer);
    high_value_customers = [order["customer"] for order in orders if order["total"] >= 100]
    print(high_value_customers)

    # TODO 4: list of delivered order IDs 🔞 
    # TS: const deliveredIds = orders.filter((order) => order.status === 'delivered).map(order => order.id)
    delivered_ids = [order["id"] for order in orders if order["status"] == "delivered"]
    print(delivered_ids)


main()
