input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

frequency = {}

for item in input_list:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency count:", frequency)
