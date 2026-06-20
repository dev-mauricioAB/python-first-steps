# basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")

# catching multiple exceptions
def parse(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number")
        return -1

parse("42")   # 42
parse("abc")  # prints error, returns -1

# finally — always runs, even if there's an error
def read_file(path: str) -> str:
    try:
        f = open(path)
        return f.read()
    except FileNotFoundError:
        return "file not found"
    finally:
        print("read attempt finished")  # always runs

# raising your own exception
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # "cannot divide by zero"

# TypeScript parallel:
# TS
# try { ... } catch (e) { ... } finally { ... }
# throw new Error("message")

# Python
# try: ... except SomeError as e: ... finally: ...
# raise ValueError("message")