start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
odd_sum = sum(i for i in range(start, stop + 1) if i % 2 != 0)
print(f"Sum of odd numbers between {start} and {stop}: {odd_sum}")