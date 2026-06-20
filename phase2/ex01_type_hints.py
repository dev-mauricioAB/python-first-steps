# Exercise 1 — Type Hints
# Practice: annotate all function parameters and return types


def full_name(first: str, last: str) -> str:
    # TODO: return "First Last"
    pass


def is_adult(age: int) -> bool:
    # TODO: return True if age >= 18
    pass


def average(numbers: list[float]) -> float:
    # TODO: return the average of the list
    pass


def main():
    print(full_name("Mauricio", "AB"))   # "Mauricio AB"
    print(is_adult(20))                  # True
    print(is_adult(15))                  # False
    print(average([10.0, 20.0, 30.0]))   # 20.0


main()
