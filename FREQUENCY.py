xyz = input("Letter you want to count: ")
string = input("Enter the string: ")
count = 0
for i in string:
    if i == xyz:
        count += 1
print(count)
