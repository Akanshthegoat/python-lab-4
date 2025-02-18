
input_str = input("Enter a string: ").lower()
a_count = e_count = i_count = o_count = u_count = 0


for char in input_str:
    if char == 'a':
        a_count += 1
    elif char == 'e':
        e_count += 1
    elif char == 'i':
        i_count += 1
    elif char == 'o':
        o_count += 1
    elif char == 'u':
        u_count += 1


print(f"Frequency of 'a': {a_count}")
print(f"Frequency of 'e': {e_count}")
print(f"Frequency of 'i': {i_count}")
print(f"Frequency of 'o': {o_count}")
print(f"Frequency of 'u': {u_count}")
