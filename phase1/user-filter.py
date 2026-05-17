# 1. User filter CLI
# Build a script that reads users.json, accepts a status like active or inactive, and prints only
# matching users as formatted JSON.
# 
# Skills:
# - file reading
# - JSON parsing
# - loop/filter logic
# - CLI args
# - exception handling
# 
# Example usage:
# ``python user_filter.py --status active``


import argparse
import json

from phase1.user import User, UserData

parse = argparse.ArgumentParser(
  description="Provider an user status"
)

parse.add_argument(
  "-s", "--status", metavar="status",
  required=True, help="User status"
)

args = parse.parse_args()

msg = f"arg >> {args.status}!"
print(msg)

def read_user_json(path: str):
  try:
    with open(path, "r") as f:
      raw_data: UserData = json.load(f)      
      # Convert dict to User objects
      users: list[User] = [
          User(**user_dict) for user_dict in raw_data["data"]
      ]
      
      usersFiltered = [
          user for user in users 
          if user.active is True  # ← AUTOCOMPLETE WORKS HERE! 
      ]
    
      print(usersFiltered)
      return usersFiltered
  except FileNotFoundError:
    print(f"File {path} not exist. Creating empty list.")
    return []
  except json.JSONDecodeError as e:
    print(f"Error while decoding {f}. Invalid JSON: {e}")
    return[]
  
users: list[User] = read_user_json("users.json")

# Now you get autocomplete!
for user in users:
    if user.active:  # Type hint tells IDE: "active" is a bool field
        print(user.name)  # TAB here → shows all User fields