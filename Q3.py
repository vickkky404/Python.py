# Wap to count number of words present in a string and count how many word starting with S.
input_String = input("Enter the String:  ")

words = input_String.split()
total_words = len(words)
words_s = 0

for word in words:
    if word.lower().startswith('s'):  # Check if the word starts with 'S' or 's'
        words_starting_with_s += 1

# Display the results
print("Total number of words:", total_words)
print("Number of words starting with 'S':", words_starting_with_s)




