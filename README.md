# Performance improvement tracker

This tiny project demonstrates common performance wins. It intentionally includes one hot path that is optimized with memoization to make common repeated work faster without changing behavior.

## 10 performance improvements to consider
1. Memoize repeated expensive computations.
2. Replace nested loops with set/dictionary lookups.
3. Minimize object creation inside tight loops.
4. Batch database queries instead of issuing one query per row.
5. Avoid repeated parsing of constant configuration values.
6. Use efficient string concatenation or join for large payloads.
7. Add indexes to hot query paths.
8. Move work off the request thread with async processing or background jobs.
9. Cache user/session data near the read path.
10. Limit full scans by filtering earlier and paging large result sets.

## The chosen improvement
The highest-impact, lowest-effort optimization here is number 1: memoize repeated expensive calculations in the hot path.

The public API is intentionally tiny: `rank_values` takes a list of integers and returns the prime-valued records ranked by their total divisor sum.

## Quick usage
```python
from src.performance_demo import rank_values

print(rank_values([2, 3, 4, 5, 6, 7, 7, 10]))
```
