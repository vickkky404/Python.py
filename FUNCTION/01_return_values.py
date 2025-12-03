# Functions with Return Values

# Single return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Addition: {result}")

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")

# Return dictionary
def calculate(a, b):
    return {
        'sum': a + b,
        'diff': a - b,
        'product': a * b,
        'division': a / b
    }

results = calculate(10, 2)
for key, value in results.items():
    print(f"{key}: {value}")

# Early return
def validate_number(num):
    if not isinstance(num, int):
        return False
    if num < 0:
        return False
    return True

print(f"\nValidate 5: {validate_number(5)}")
print(f"Validate -5: {validate_number(-5)}")
print(f"Validate 'abc': {validate_number('abc')}")
