# Polygon Area Calculator

A Python OOP project implementing a `Rectangle` class and a `Square` subclass with geometric calculation methods.

## Objective

Implement both classes so that all 22 tests pass.

---

## Classes

### `Rectangle`

Initialised with `width` and `height`.

#### Methods

**`set_width(width)`**
Sets the rectangle's width.

**`set_height(height)`**
Sets the rectangle's height.

**`get_area()`**
Returns `width × height`.

**`get_perimeter()`**
Returns `2 × (width + height)`.

**`get_diagonal()`**
Returns `√(width² + height²)`.

**`get_picture()`**
Returns a string representation of the shape using lines of `*`. The number of lines equals the height; the number of `*` per line equals the width. Each line ends with `\n`. Returns `Too big for picture.` if either dimension exceeds 50.

**`get_amount_inside(shape)`**
Accepts another `Rectangle` or `Square` instance. Returns the number of times the passed shape fits inside this shape with no rotations.

#### String representation

```
Rectangle(width=5, height=10)
```

---

### `Square` (subclass of `Rectangle`)

Initialised with a single `side` length, stored in both `width` and `height`.

#### Methods

**`set_width(side)`**
Overrides the parent method. Sets both width and height to the given side length.

**`set_height(side)`**
Overrides the parent method. Sets both width and height to the given side length.

**`set_side(side)`**
Sets both width and height to the given side length.

The `Square` class inherits all other methods from `Rectangle`.

#### String representation

```
Square(side=9)
```

---

## Usage Example

```python
rect = Rectangle(10, 5)
print(rect.get_area())       # 50
rect.set_height(3)
print(rect.get_perimeter())  # 26
print(rect)                  # Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********

sq = Square(9)
print(sq.get_area())         # 81
sq.set_side(4)
print(sq.get_diagonal())     # 5.656854249492381
print(sq)                    # Square(side=4)
print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8
```

---

## Tests

| # | Test |
|---|------|
| 1 | `Rectangle` class exists |
| 2 | `Square` class exists |
| 3 | `Square` is a subclass of `Rectangle` |
| 4 | `Square` is a distinct class from `Rectangle` |
| 5 | A `Square` instance is an instance of both `Square` and `Rectangle` |
| 6 | `str(Rectangle(3, 6))` returns `Rectangle(width=3, height=6)` |
| 7 | `str(Square(5))` returns `Square(side=5)` |
| 8 | `Rectangle(3, 6).get_area()` returns `18` |
| 9 | `Square(5).get_area()` returns `25` |
| 10 | `Rectangle(3, 6).get_perimeter()` returns `18` |
| 11 | `Square(5).get_perimeter()` returns `20` |
| 12 | `Rectangle(3, 6).get_diagonal()` returns `6.708203932499369` |
| 13 | `Square(5).get_diagonal()` returns `7.0710678118654755` |
| 14 | A `Rectangle` instance has a different string representation after updating values |
| 15 | A `Square` instance has a different string representation after calling `.set_side()` |
| 16 | A `Square` instance has a different string representation after calling `.set_width()` or `.set_height()` |
| 17 | `get_picture()` returns the correct string for a `Rectangle` |
| 18 | `get_picture()` returns the correct string for a `Square` |
| 19 | `get_picture()` returns `Too big for picture.` when width or height exceeds 50 |
| 20 | `Rectangle(15, 10).get_amount_inside(Square(5))` returns `6` |
| 21 | `Rectangle(4, 8).get_amount_inside(Rectangle(3, 6))` returns `1` |
| 22 | `Rectangle(2, 3).get_amount_inside(Rectangle(3, 6))` returns `0` |
