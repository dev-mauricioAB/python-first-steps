numbers = [1, 2, 3, 4, 5, 6]

# --- list comprehension ---
# [expression for item in iterable]
doubled = [n * 2 for n in numbers]
# [2, 4, 6, 8, 10, 12]

# with filter
# [expression for item in iterable if condition]
evens = [n for n in numbers if n % 2 == 0]
# [2, 4, 6]

# --- dict comprehension ---
# {key: value for item in iterable}
squared = {n: n ** 2 for n in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# real backend example — reshape a list of dicts
users = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 17},
    {"name": "carol", "age": 32},
]

# extract just names in uppercase
names = [u["name"].upper() for u in users]
# ["ALICE", "BOB", "CAROL"]

# filter adults only
adults = [u for u in users if u["age"] >= 18]
# [{"name": "alice", ...}, {"name": "carol", ...}]

# build a dict of name -> age
name_age = {u["name"]: u["age"] for u in users}
# {"alice": 25, "bob": 17, "carol": 32}


# TypeScript parallel:
# JS/TS
# const doubled = numbers.map(n => n * 2)
# const evens = numbers.filter(n => n % 2 === 0)

# Python
# doubled = [n * 2 for n in numbers]
# evens = [n for n in numbers if n % 2 == 0]