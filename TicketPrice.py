# ask for age to the customer
age = int(input("Enter your age: "))

# apply the condational statement
if age < 0:
    print("Invalid Age!")
elif age < 12:
    ticket_price = 100
elif age < 18:
    ticket_price = 150
elif age < 60:
    ticket_price = 200
else:
    ticket_price = 120

# display the final ticket price to user according to the user...
if age >= 0:
    print(f"Your ticket price is ₹{ticket_price}.")
