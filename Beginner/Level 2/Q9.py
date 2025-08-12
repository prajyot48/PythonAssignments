try:
    sample_list = [10, 20, 30]
    index = int(input("Enter an index: "))
    print("Element at index", index, "is", sample_list[index])
except IndexError:
    print("Error: Index out of range.")
