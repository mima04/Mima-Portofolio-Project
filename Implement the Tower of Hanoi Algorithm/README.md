# Tower of Hanoi

A Python implementation of the classic Tower of Hanoi mathematical puzzle using a recursive algorithm.

## The Puzzle

Three rods and `n` disks of different sizes start stacked on the first rod in decreasing order (largest at the bottom, smallest at the top). The goal is to move the entire stack to the third rod following three rules:

1. Only the top-most disk on any rod may be moved
2. Only one disk may be moved at a time
3. A larger disk may never be placed on top of a smaller one

---

## Objective

Implement `hanoi_solver` so that all 8 tests pass.

---

## Function

### `hanoi_solver(n)`

Takes a single integer `n` representing the total number of disks.

- Solves the puzzle in exactly `2ⁿ - 1` moves
- Returns a string of every state (starting arrangement included), one per line
- Each state shows all three rods as space-separated lists of integers, where `1` is the smallest disk
- The returned string ends with a trailing newline

**Example — `hanoi_solver(3)`:**

```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

**Example — `hanoi_solver(2)`:**

```
[2, 1] [] []
[2] [1] []
[] [1] [2]
[] [] [2, 1]
```

---

## Tests

| # | Test |
|---|------|
| 1 | A function named `hanoi_solver` is defined |
| 2 | `hanoi_solver` accepts a single argument |
| 3 | `hanoi_solver` returns a string |
| 4 | `hanoi_solver(2)` returns the correct 3-move sequence |
| 5 | `hanoi_solver(3)` returns the correct 7-move sequence |
| 6 | `hanoi_solver(4)` returns the correct 15-move sequence |
| 7 | `hanoi_solver(5)` returns the correct 31-move sequence |
| 8 | `hanoi_solver(n)` solves the puzzle correctly for any positive integer `n` |
