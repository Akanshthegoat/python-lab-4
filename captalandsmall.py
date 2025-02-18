sample_string = input("Enter a string: ")

words = sample_string.split()


result = []
for word in words:
    if len(word) > 1:
        word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        word = word.upper()
    result.append(word)


output_string = " ".join(result)
print("Result:", output_string)
