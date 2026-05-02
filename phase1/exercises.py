# 1. Variables
# Declare these with type hints: user_age (int=30), is_premium (bool=True), tags
# (list[str]=["python","backend"]), profile (dict[str, any] with name/email/age).
# Print using f-string.
user_age: int = 32
is_premium: bool = True
tags: list[str] = ["python", "backend"]

print("----- EXERCISE 1 -----")
print(f"User age: {user_age} \nIs Premium: {is_premium} \nTags: {tags}")

# 2. Functions
# Write greet_user(name: str, is_new: bool = False) -> str that returns "Welcome back,
# Alice!" or "Welcome, Alice!".
def greet_user(name: str, is_new: bool = False):
  if(is_new):
    print(f"Welcome, {name}")
  else:
    print(f"Welcome back, {name}")
    # match is_new:
    #     case True:
    #         print(f"Welcome, {name}")
    #     case False:
    #         print(f"Welcome back, {name}")
  
print("----- EXERCISE 2 -----")
greet_user("Raquel", True)

# 3. Control Flow
# Given scores = [85, 92, 78, 101, 45], use loop + if to print "Pass" (>70) or "Fail" for each,
# count passes.
def control_passes(scores: list[int]):
  for score in scores:
    if(score > 70):
      print(f"{score} Pass :)")
    else:
      print(f"{score} Fail :(")

scores = [84,92,78,101,45]
print("----- EXERCISE 3 -----")
control_passes(scores)

# 4. List Comprehension
# From users = [{"name": "alice", "active": True}, {"name": "bob", "active": False}],
# create active_names = [u["name"].upper() for u in users if u["active"]].
users = [
  {"name": "alice", "active": True, "saldo": 100}, 
  {"name": "bob", "active": False, "saldo": 80},
  {"name": "john", "active": True, "saldo": 70},
  {"name": "jose", "active": True, "saldo": 50},
]
active_names = [user["name"] for user in users if user["active"] and user["saldo"] >= 70]
print("----- EXERCISE 4 -----")
print(f"Active users: {active_names}")

# 5. Dictionary Manipulation
# user = {"name": "alice", "score": 85}. Add "status": "active". Update score +=10. Print keys
# as list.
user = {"name": "alice", "score": 60}
user.update({
  "status": "Active" if user["score"] > 80 else "Disabled",
  "score": user["score"] + 10
})

print("----- EXERCISE 5 -----")
print(f"USER > {user}")

# 6. Multiple Exceptions
# Write safe_divide(a: float, b: float) -> float that handles ZeroDivisionError ("Can't
# divide by zero") and TypeError ("Inputs must be numbers").
def safe_divide(a: float, b: float):
  result = a / b

  if(result is ZeroDivisionError):
    raise ZeroDivisionError("Can't divide by zero")
  
  if(result is TypeError):
    raise TypeError("Inputs must be numbers")
  
  print(f"Result: {result}")

print("----- EXERCISE 6 -----")
safe_divide(2,1)
# safe_divide("2",1)
# safe_divide(2,0)

# 7. File Simulation
# Simulate reading config: config_str = '{"host": "localhost", "port": 8080}'. Use
# json.loads() to parse, print host/port or handle JSONDecodeError.
import json

def load_str_to_json(value: str):
  loaded = json.loads(value)

  if(loaded is json.JSONDecodeError):
    raise json.JSONDecodeError(loaded)
  
  print(loaded)
  
print("----- EXERCISE 7 -----")
config_str = '{"host": "localhost", "port": 8080}'
load_str_to_json(config_str)

# 8. Modules Pattern
# Write stats.py with def count_active(users: list[dict]) -> int:. Test in test.py
# importing it. Return count of "status": "active".
...

# 9. Mixed Collections
# orders = [{"id": 1, "items": ["book", "pen"]}, {"id": 2, "items": ["laptop"]}].
# Flatten to single list of all items using comprehension.
print("----- EXERCISE 9 -----")
orders = [{"id": 1, "items": ["book", "pen"]}, {"id": 2, "items": ["laptop"]}]
all_items = []
for order in orders:
  for item in order["items"]:
    all_items.append(item)
    
print(f"All items: {all_items}")

# 10. Backend Data Processor
# Complete function processing API response:
def process_api_response(data: list[dict]) -> dict:
    actives = []
    avg_score = 0

    for d in data:
      if(d["active"] is True):
        actives.append(d)
        avg_score += d["score"]
    
    to_return = {
      "active_count": actives.__len__(),
      "avg_score": avg_score / actives.__len__()
    }

    print(to_return)
      
    # Filter active, calc avg score, return {"active_count": X, "avg_score": Y}
    pass

print("----- EXERCISE 10 -----")
data = [
  {'name': 'a', 'active': True, 'score': 85}, 
  {'name': 'b', 'active': False, 'score': 90}
]
process_api_response(data)
