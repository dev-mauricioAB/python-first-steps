import json

def load_orders(path: str) -> list[dict]:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"file not found: {path}")

def summarize(orders: list[dict]) -> dict:
    delivered = [o for o in orders if o["status"] == "delivered"]
    return {
        "total": len(orders),
        "delivered": len(delivered),
        "revenue": sum(o["total"] for o in delivered),
    }

def main():
    orders = load_orders("orders.json")
    result = summarize(orders)
    print(result)

main()