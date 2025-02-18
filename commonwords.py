
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

words1 = set(str1.split())
words2 = set(str2.split())

common = words1.intersection(words2)

if common:
    print("Common words:", ", ".join(common))
else:
    print("No common words found.")
