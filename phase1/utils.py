def calculate_average(scores: list[int]) -> float:
    if not scores:
        raise ValueError("No scores provided")
    return sum(scores) / len(scores)