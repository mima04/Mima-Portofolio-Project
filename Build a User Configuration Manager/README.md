# User Configuration Manager

A Python utility for managing user settings (theme, language, notifications, etc.) through a set of functions that add, update, delete and view configuration preferences.

## Objective

Implement four functions and a test dictionary so that all 27 tests pass.

---

## Setup

Create a dictionary named `test_settings` to store user configuration preferences for testing:

```python
test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}
```

---

## Functions

### `add_setting(settings, kv_pair)`

Adds a new key-value pair to the settings dictionary.

- Converts both key and value to lowercase
- If the key already exists: returns `Setting '[key]' already exists! Cannot add a new setting with this name.`
- If the key does not exist: adds the pair and returns `Setting '[key]' added with value '[value]' successfully!`

**Examples:**

```python
add_setting({'theme': 'light'}, ('THEME', 'dark'))
# "Setting 'theme' already exists! Cannot add a new setting with this name."

add_setting({'theme': 'light'}, ('volume', 'high'))
# "Setting 'volume' added with value 'high' successfully!"
```

---

### `update_setting(settings, kv_pair)`

Updates the value of an existing key in the settings dictionary.

- Converts both key and value to lowercase
- If the key exists: updates the value and returns `Setting '[key]' updated to '[value]' successfully!`
- If the key does not exist: returns `Setting '[key]' does not exist! Cannot update a non-existing setting.`

**Examples:**

```python
update_setting({'theme': 'light'}, ('theme', 'dark'))
# "Setting 'theme' updated to 'dark' successfully!"

update_setting({'theme': 'light'}, ('volume', 'high'))
# "Setting 'volume' does not exist! Cannot update a non-existing setting."
```

---

### `delete_setting(settings, key)`

Removes a key-value pair from the settings dictionary.

- Converts the key to lowercase
- If the key exists: removes the pair and returns `Setting '[key]' deleted successfully!`
- If the key does not exist: returns `Setting not found!`

**Examples:**

```python
delete_setting({'theme': 'light'}, 'theme')
# "Setting 'theme' deleted successfully!"

delete_setting({'theme': 'light'}, 'volume')
# "Setting not found!"
```

---

### `view_settings(settings)`

Returns a formatted string of all current settings.

- If the dictionary is empty: returns `No settings available.`
- Otherwise: returns a string beginning with `Current User Settings:` followed by each key-value pair on a new line, with the key capitalised
- The output must end with a newline character

**Example:**

```python
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
```

```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

---

## Tests

| # | Test |
|---|------|
| 1 | `test_settings` dictionary exists and contains values |
| 2 | `add_setting` function is defined |
| 3 | `add_setting` has two parameters |
| 4 | `add_setting` converts the key to lowercase |
| 5 | `add_setting` converts the value to lowercase |
| 6 | `add_setting` returns the correct error message when the key already exists |
| 7 | `add_setting` returns the correct success message when the key is new |
| 8 | `add_setting` correctly adds the key-value pair to the dictionary |
| 9 | `update_setting` function is defined |
| 10 | `update_setting` has two parameters |
| 11 | `update_setting` converts the key to lowercase |
| 12 | `update_setting` converts the value to lowercase |
| 13 | `update_setting` returns the correct success message when the key exists |
| 14 | `update_setting` returns the correct error message when the key does not exist |
| 15 | `update_setting` correctly updates the key-value pair in the dictionary |
| 16 | `delete_setting` function is defined |
| 17 | `delete_setting` has two parameters |
| 18 | `delete_setting` converts the key to lowercase |
| 19 | `delete_setting` returns the correct success message when the key exists |
| 20 | `delete_setting` returns the correct error message when the key does not exist |
| 21 | `delete_setting` correctly removes the key from the dictionary |
| 22 | `view_settings` function is defined |
| 23 | `view_settings` has one parameter |
| 24 | `view_settings` returns `No settings available.` for an empty dictionary |
| 25 | `view_settings` returns correctly formatted settings for a non-empty dictionary |
| 26 | `view_settings` capitalises the first letter of each setting name |
| 27 | `view_settings` output ends with a newline character |
