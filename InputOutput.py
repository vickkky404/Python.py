# input of grocery items(5 items)
item1 = float(input("Enter price of First item:"))
item2 = float(input("Enter price of First item:"))
item3 = float(input("Enter price of First item:"))
item4 = float(input("Enter price of First item:"))
item5 = float(input("Enter price of First item:"))


# calcullate the total amount of 5 items..
total_amount = item1 + item2 + item3 + item4 + item5

# calculate if the discount is applicable or not , if the amount will crossrs 500 then 10%discount will be valid..
if total_amount >500:
    discount = total_amount * 0.1
    final_amount = total_amount - discount
    print(f"Total cost: ₹{total_amount:.2f}")
    print(f"Discount: ₹{discount:.2f}") 
else:
    final_amount = total_amount
    
    print("No discount applicable")


# print the final amount
print(f"Total cost: ₹{total_amount:.2f}")
print("Happy Shooping!!")