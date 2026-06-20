def calculate_average(scores: list[int]) -> float:
    if not scores:
        raise ValueError("No scores provided")
    return sum(scores) / len(scores)

def format_name(first: str, last: str):
    f_formated = first.capitalize()
    l_formated = last.capitalize()
    to_return = f"{f_formated}, {l_formated}"
    return to_return