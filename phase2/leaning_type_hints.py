# 1. Type Hints
# Python is dynamically typed — but you can (and should) annotate
# types to make code readable and catch errors early. Same idea as TypeScript.

# without type hints — works but unclear
def greet(name):
    return "Hello " + name

# with type hints — clear contract, just like TypeScript
def greet(name: str) -> str:
    return "Hello " + name

# parameters
def add(a: int, b: int) -> int:
    return a + b

# optional value (can be str or None)
def find_user(id: int) -> str | None:
    if id == 1:
        return "Mauricio"
    return None

# list, dict, tuple
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def get_user() -> dict[str, str]:
    return {"name": "Mauricio", "email": "m@email.com"}

# TypeScript parallel:
# function greet(name: string): string { ... }  // TS
# def greet(name: str) -> str: ...              # Python