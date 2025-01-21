# 21-1-25 write a progeam to check a string is palindrome or not by using slicing operator

string = input("Enter the string to cheeck whether it is palindrome or not: ")
if string == string[::-1]:
    print("The string is palindrome....")
else:
    print("The string is not palindrome...")
    
    
