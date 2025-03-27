# Assignment: Django Signals & Custom Classes

## Topic 1: Django Signals

### Question 1: Are Django signals executed synchronously by default?
Yes, Django signals run synchronously by default.

**Proof:** In `test_sync_execution`, we delay the signal and observe total time.

### Question 2: Do signals run in the same thread?
Yes. Using `threading.get_ident()` we verify both caller and signal share the same thread.

### Question 3: Do signals run in the same DB transaction?
Yes. Any DB write in a signal will be rolled back if the outer transaction fails.

**Proof:** See `test_transaction_scope`.

## Topic 2: Rectangle Class

### Requirements
- Init with `length`, `width`
- Iterable yielding:
  ```python
  {'length': value}, {'width': value}
  ```

**Implemented in:** `rectangle.py`

### Example:
```python
r = Rectangle(5, 3)
for item in r:
    print(item)
```

**Output:**
```
{'length': 5}
{'width': 3}
