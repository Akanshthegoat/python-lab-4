sample_string = input("Enter a string: ")

if sample_string == sample_string[::-1]:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")