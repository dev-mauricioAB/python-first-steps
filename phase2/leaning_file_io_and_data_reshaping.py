import json

# --- reading a text file ---
with open("notes.txt", "r") as f:
    content = f.read()       # full content as string
    # or
    lines = f.readlines()    # list of lines

# --- writing a text file ---
with open("output.txt", "w") as f:
    f.write("hello world\n")

# --- reading JSON ---
with open("data.json", "r") as f:
    data = json.load(f)      # parses JSON into dict/list

# --- writing JSON ---
result = {"name": "Mauricio", "score": 99}
with open("result.json", "w") as f:
    json.dump(result, f, indent=2)

# --- reshaping data ---
orders = [
    {"customer": "Alice", "total": 100.0, "status": "delivered"},
    {"customer": "Bob",   "total": 50.0,  "status": "pending"},
]

# keep only delivered, add tax
summary = [
    {"customer": o["customer"], "total_with_tax": o["total"] * 1.1}
    for o in orders
    if o["status"] == "delivered"
]
# [{"customer": "Alice", "total_with_tax": 110.0}]