# Default Parameter Values

# Simple defaults
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# Multiple defaults
def create_profile(name, age=18, city="Unknown", country="India"):
    return f"Name: {name}, Age: {age}, City: {city}, Country: {country}"

print(create_profile("John"))
print(create_profile("Jane", 25, "Mumbai"))
print(create_profile("Jack", 30, country="USA"))

# Default with mutable types (tricky!)
def add_to_list(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_to_list(1)
list2 = add_to_list(2)
print(f"List1: {list1}")
print(f"List2: {list2}")

# Function as default
def apply_operation(a, b, operation=lambda x, y: x + y):
    return operation(a, b)

print(f"Addition: {apply_operation(5, 3)}")
print(f"Multiplication: {apply_operation(5, 3, lambda x, y: x * y)}")
