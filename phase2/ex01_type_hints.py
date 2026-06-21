# Exercise 1 — Type Hints
# Practice: annotate all function parameters and return types


def full_name(first: str, last: str) -> str:
    return f"{first.title()} {last.title()} "


def is_adult(age: int) -> bool:
    # TODO: return True if age >= 18
    if age >= 18:
        return True
    return False

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def main():
    print(full_name("mauricio", "alexandre"))   # "Mauricio Alexandre"
    print(is_adult(20))                         # True
    print(is_adult(15))                         # False
    print(average([10.0, 20.0, 30.0]))          # 20.0


main()
