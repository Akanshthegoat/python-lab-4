
input_str = input("Enter a string: ")

words = input_str.split()

smallest_word = min(words, key=len)

print(f"The smallest word is: {smallest_word}")
