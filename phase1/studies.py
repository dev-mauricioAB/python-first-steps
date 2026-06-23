import json

# -------------------------------------------
user_id: int = 123
username: str = "mauricio"
is_active: bool = True
scores: list = [85, 92, 78]
user_info: dict = {"id": user_id, "name": username, "active": is_active}

print(f"User {user_info['name']} (ID: {user_id}) scores: {scores}")
print(type(scores))  # Check type


# -------------------------------------------
def filter_active_users(users: list[dict]) -> list[dict]:
    active = []
    for user in users:
        if user.get("status") == "active":
            active.append(user)
    return active

# Test data
users = [
    {"name": "Alice", "status": "active"},
    {"name": "Bob", "status": "inactive"},
    {"name": "Charlie", "status": "active"}
]

print(filter_active_users(users))


# -------------------------------------------
users = [{"name": "alice", "score": 85}, {"name": "bob", "score": 92}, {"name": "charlie", "score": 78}]

# Uppercase names, filter high scores
high_scorers = [{"name": u["name"].upper(), "score": u["score"]} for u in users if u["score"] > 80]
print(high_scorers)


# -------------------------------------------

def load_users(filename: str) -> list[dict]:
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found. Creating empty list.")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return []

users = load_users("users.json")
print(f"Loaded {len(users)} users")