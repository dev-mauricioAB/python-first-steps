# Exercise 3 — Exceptions
# Practice: raise errors, catch specific exceptions, use try/except/finally


def divide(a: float, b: float) -> float:
    # TODO: raise ValueError if b is zero, otherwise return a / b
    # TS:
    # function divide(a: number, b: number): number {
    #   if (b === 0) throw new Error("Can't divide by zero");
    #  return a / b;
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b


def safe_parse_int(value: str) -> int:
    # TODO: try to convert value to int, return -1 if it fails
    # function safeParseInt(value: string): number {
    #   const parsed = Number.parseInt(value, 10);
    #   return Number.isNaN(parsed) ? -1 : parsed;
    try:
        return int(value)
    except ValueError:
        return -1


def get_item_safe(items: list[stg], index: int) -> str:
    # TODO: return items[index], but catch IndexError and return "not found"
    # TS:
    # function getItemSafe(items: string[], index: number): string {
    #   return index >= 0 && index < items.length ? items[index] : "not found";
    try:
        return items[index]
    except IndexError:
        return "not found"

def parse_float_or_default(value: str, default: float) -> float:
    # TODO: try to convert value to float; if ValueError happens, return default
    # TS:
    # function parseFloatOrDefault(value: string, default: number): number {
    #   const parsed = Number.parseFloat(value);
    #   return Number.isNaN(parsed) ? default : parsed;
    try:
        return float(value)
    except ValueError:
        return default


def validate_age(age: int) -> int:
    # TODO: raise VallueError if age is negative, otherwise return age
    # TS:
    # function validateAge(age: number): number {
    #   if(age <0) throw new Error("Age cannot be negative");
    #   return age;
    # }
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


def safe_divisor_with_finally(a: float, b: float) -> float:
    # TODO: implement a function that divides a by b, using try/except/finally
    # TS:
    # function safeDivisorWithFinally(a: number, b: number): number {
    #   try {
    #     if (b === 0) throw new Error("Can't divide by zero");
    #     return a / b;
    #   } finally {
    #     console.log("Division operation completed");
    #   }
    # }
    try:
        if b == 0:
            raise ValueError("Can't divide by zero")
        return a / b
    except ValueError as e:
        print(f"Error: {e}")
        raise
    finally:
        print("Division operation completed")


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

    # TODO 1: index access with IndexError handling
    items = ["apple", "banana", "cherry"]
    print(get_item_safe(items, 1))  # banana
    print(get_item_safe(items, 5))  # not found

    # TODO 2: parse float with default
    print(parse_float_or_default("3.14", 0.0))  # 3.14
    print(parse_float_or_default("abc", 0.0))   # 0.

    # TODO 3: validate age
    print(validate_age(25))   # 25
    try:
        print(validate_age(-5))
    except ValueError as e:
        print(f"Error: {e}")

    # TODO 4: safe divisor with finally
    print(safe_divisor_with_finally(10, 2))  # 5
    try:
        print(safe_divisor_with_finally(10, 0))
    except ValueError as e:
        print(f"Error: {e}")

main()
