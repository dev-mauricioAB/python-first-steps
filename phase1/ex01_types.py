# ex01_types.py

def main():
    # str — text manipulation
    name: str = "mauricio"
    print(name.upper())           # "MAURICIO" — uppercase
    print(name.capitalize())      # "Mauricio" — first letter uppercase
    print(name.replace("o", "0")) # "maurici0" — replace chars
    print(len(name))              # 8 — character count
    print(name.startswith("mau")) # True — check prefix

    # int — math operations
    age: int = 30
    print(abs(-age))              # 30 — absolute value
    print(pow(age, 2))            # 900 — power
    print(age % 7)                # 2 — remainder (modulo)

    # float — rounding and precision
    height: float = 1.756
    print(round(height, 2))       # 1.76 — round to 2 decimals
    print(int(height))            # 1 — truncate decimal part

    # bool — logical operations
    is_active: bool = True
    print(not is_active)          # False — invert
    print(is_active and False)    # False — both must be True
    print(is_active or False)     # True — at least one must be True

    # list — ordered and mutable
    skills: list = ["python", "typescript", "docker"]
    skills.append("fastapi")      # add to end
    skills.remove("docker")       # remove by value
    print(skills[0])              # "python" — access by index
    print(len(skills))            # 3 — count items
    print("python" in skills)     # True — check existence
    skills.sort()                 # sort alphabetically in place
    print(skills)

    # dict — key-value access
    user: dict = {"name": "Mauricio", "age": 30}
    print(user["name"])           # "Mauricio" — access by key
    print(user.get("email", "no email"))  # safe access with default
    user["email"] = "m@email.com" # add new key
    print(user.keys())            # all keys
    print(user.values())          # all values
    print(user.items())           # all key-value pairs as tuples

    # tuple — immutable sequence
    coordinates: tuple = (40.7128, -74.0060)
    print(coordinates[0])         # 40.7128 — access by index
    print(len(coordinates))       # 2 — count items
    print(coordinates.count(40.7128))  # 1 — how many times a value appears

    # set — unique values only
    tags: set = {"backend", "api", "backend"}
    tags.add("python")            # add item (ignored if already exists)
    tags.discard("api")           # remove without error if missing
    print(len(tags))              # count unique items
    print("backend" in tags)      # True — check membership

    other_tags: set = {"python", "cloud"}
    print(tags.union(other_tags))        # all items from both sets
    print(tags.intersection(other_tags)) # only items in both sets


main()