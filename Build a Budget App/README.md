# Budget App

A Python budget tracker that monitors spending across categories and visualises relative spend as a bar chart.

## Objective

Implement the `Category` class and `create_spend_chart()` function so that all 24 tests pass.

---

## User Stories

### 1. Category Class

The `Category` class accepts a single `name` argument and exposes an instance attribute `ledger` (a list of transaction objects).

#### Methods

**`deposit(amount, description='')`**
Appends `{'amount': amount, 'description': description}` to the ledger.

**`withdraw(amount, description='')`**
Stores the amount as a negative number in the ledger. Returns `True` if the withdrawal succeeded, `False` otherwise.

**`get_balance()`**
Returns the current balance calculated from all ledger entries.

**`transfer(amount, category)`**
Withdraws `amount` with description `Transfer to [Destination]` and deposits it into `category` with description `Transfer from [Source]`. Returns `True` on success, `False` otherwise.

**`check_funds(amount)`**
Returns `False` if `amount` exceeds the current balance, `True` otherwise. Must be used by both `withdraw` and `transfer`.

---

### 2. String Representation

When a `Category` instance is printed it should output:

- A 30-character title line with the category name centred between `*` characters
- Each ledger entry: description left-aligned (max 23 chars) and amount right-aligned (max 7 chars, 2 decimal places)
- A final `Total: [balance]` line

**Example:**

```
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

**Output:**

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

---

### 3. `create_spend_chart(categories)`

A standalone function that accepts a list of `Category` instances and returns a bar-chart string.

**Rules:**

- Title: `Percentage spent by category`
- Percentages are based on withdrawals only (not deposits), each rounded **down** to the nearest 10
- Y-axis labels run from `100` down to `0` in steps of 10
- Bars use `o` characters
- A horizontal line appears two spaces past the last bar
- Category names are written **vertically** below their bar
- Function accepts up to four categories
- The returned string must **not** end with a newline character
- Every line must be the same length; bars are separated by two spaces with two additional spaces after the final bar

**Example output:**

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

---

## Tests

| # | Test |
|---|------|
| 1 | `deposit` creates the correct ledger object |
| 2 | `deposit` with no description defaults to blank |
| 3 | `withdraw` creates the correct ledger object |
| 4 | `withdraw` with no description defaults to blank |
| 5 | `withdraw` returns `True` on success |
| 6 | Balance is `854.33` after depositing `900` and withdrawing `45.67` |
| 7 | `transfer` creates the correct ledger item in the source category |
| 8 | `transfer` returns `True` on success |
| 9 | `transfer` reduces the source category balance |
| 10 | `transfer` increases the destination category balance |
| 11 | `transfer` creates the correct ledger item in the destination category |
| 12 | `check_funds` returns `False` when amount exceeds balance |
| 13 | `check_funds` returns `True` when amount does not exceed balance |
| 14 | `withdraw` returns `False` when funds are insufficient |
| 15 | `transfer` returns `False` when funds are insufficient |
| 16 | Printing a `Category` instance produces the correct string |
| 17 | Chart title is `Percentage spent by category` |
| 18 | Chart has correct percentages down the left side |
| 19 | Bar heights are rounded down to the nearest 10 |
| 20 | Every chart line is the same length; bars separated by two spaces with two extra spaces after the last bar |
| 21 | Horizontal line uses three `-` per category and extends two characters past the final bar |
| 22 | Chart string does not end with a newline character |
| 23 | Category names are written vertically; lines are equal length with correct spacing |
| 24 | Full chart output matches expected spacing exactly |

> **Tip:** Open the browser console (`F12`) for verbose test output.
