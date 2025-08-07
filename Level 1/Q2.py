ui = input("Enter a string: ")

l = 0
d = 0

for c in ui:
    if c.isalpha():
        l += 1
    elif c.isdigit():
        d += 1
print(f"Alphabets: {l} & Numbers: {d}")