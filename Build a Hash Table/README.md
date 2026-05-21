# Hash Table

A Python implementation of a hash table data structure from scratch, storing key-value pairs using a character-sum hashing function.

## How It Works

The hashing function sums the Unicode values of each character in a key (via Python's built-in `ord()`). The resulting integer is used as the actual key inside an internal dictionary. Collisions (multiple keys producing the same hash) are handled by storing all matching key-value pairs in a nested dictionary under that hash value.

---

## Objective

Implement the `HashTable` class so that all 22 tests pass.

---

## Class

### `HashTable`

Initialised with a `collection` attribute set to an empty dictionary `{}`.

#### Methods

**`hash(key)`**
Takes a string and returns the sum of the Unicode values of each character.

```python
HashTable().hash('golf')  # 424
```

**`add(key, value)`**
Computes the hash of `key` and stores the key-value pair as a nested dictionary inside `collection` at that hash index. If another key already hashes to the same value, the new pair is added to the existing nested dictionary.

```python
ht = HashTable()
ht.add('rose', 'flower')
# ht.collection → { 441: { 'rose': 'flower' } }

ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')
# ht.collection → { 300: { 'fcc': 'coding', 'cfc': 'chemical' } }
```

**`remove(key)`**
Computes the hash of `key` and removes that specific key-value pair from the collection. If the key does not exist, nothing happens and no error is raised. When keys share a hash, only the targeted key is removed; the rest of the nested dictionary is preserved.

**`lookup(key)`**
Computes the hash of `key` and returns its associated value. Returns `None` if the key does not exist.

```python
ht = HashTable()
ht.add('golf', 'sport')
ht.lookup('golf')   # 'sport'
ht.lookup('bogus')  # None
```

---

## Tests

| # | Test |
|---|------|
| 1 | `HashTable` class is defined |
| 2 | A new `HashTable` instance initialises `collection` as an empty dictionary |
| 3 | `HashTable` has a `hash` method |
| 4 | `hash` takes a string as its parameter |
| 5 | `hash` returns the sum of Unicode values of each character in the string |
| 6 | `HashTable` has an `add` method |
| 7 | `add` takes a key and value as parameters |
| 8 | `HashTable` has a `remove` method |
| 9 | `remove` takes a key as its parameter |
| 10 | Removing a non-existent key does not raise an error or alter the collection |
| 11 | When multiple keys share a hash, `remove` deletes only the targeted key-value pair |
| 12 | `HashTable` has a `lookup` method |
| 13 | `lookup` takes a key as its parameter |
| 14 | `hash('golf')` returns `424` |
| 15 | `add('golf', 'sport')` stores the pair in `collection` at key `424` |
| 16 | Adding `('dear', 'friend')` and `('read', 'book')` stores both under index `412` as a nested dictionary |
| 17 | `remove` deletes the correct key and value when the key exists |
| 18 | `lookup('golf')` returns `'sport'` when the pair exists |
| 19 | `lookup('golf')` returns `None` when the pair does not exist |
| 20 | `lookup('cfc')` returns `None` when only `'fcc'` exists at that hash |
| 21 | Adding `('rose', 'flower')` produces `{ 441: { 'rose': 'flower' } }` |
| 22 | Adding two keys with the same hash produces `{ 300: { 'fcc': 'coding', 'cfc': 'chemical' } }` |
