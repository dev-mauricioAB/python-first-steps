# Exercise 3 — Exceptions
# Practice: raise errors, catch specific exceptions, use try/except/finally


def divide(a: float, b: float) -> float:
    # TODO: raise ValueError if b is zero, otherwise return a / b
    pass


def safe_parse_int(value: str) -> int:
    # TODO: try to convert value to int, return -1 if it fails
    pass


def main():
    # divide — valid case
    print(divide(10, 2))    # 5.0

    # divide — should raise and be caught here
    try:
        print(divide(10, 0))
    except ValueError as e:
        print(f"Error: {e}")

    # safe_parse_int
    print(safe_parse_int("42"))   # 42
    print(safe_parse_int("abc"))  # -1
    print(safe_parse_int("7"))    # 7


main()
