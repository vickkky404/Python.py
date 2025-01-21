name = input("Enter your name: ")
print("Hii..... this is an mini calculator made using python prograamming langauge...")
print("Enter the operation you want to perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input(f"Enter your choice, {name}: ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == '1':
    sum = a + b
    print("sum of two number is: " , sum)
elif choice == '2':
    sub = 1 - b
    print("substracton of two number is: " , sub)
elif choice == '3':
    mul = a * b
    print("Multiplication of two number is: " , mul)
elif choice == '4':
    div = a/b
    print("Division of two number is: "  , div)
    
print("Thanks for choosing mini calculator.......:)")
     