from functools import lru_cache


def _sum_divisors(value: int) -> int:
    if value < 1:
        return 0
    total = 0
    for divisor in range(1, int(value ** 0.5) + 1):
        if value % divisor == 0:
            total += divisor
            paired = value // divisor
            if paired != divisor:
                total += paired
    return total


@lru_cache(maxsize=None)
def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    limit = int(value ** 0.5)
    for candidate in range(3, limit + 1, 2):
        if value % candidate == 0:
            return False
    return True


def rank_values(values):
    """Return prime numbers ranked by the sum of their divisors."""
    scored = []
    for value in values:
        if not _is_prime(value):
            continue
        scored.append((value, _sum_divisors(value)))
    scored.sort(key=lambda item: (item[1], item[0]))
    return scored
