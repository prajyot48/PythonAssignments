input_string = input("Enter a string: ")
given_char = input("Enter a character to check: ")

starts_with = lambda s, c: s.startswith(c)

print(starts_with(input_string, given_char))
