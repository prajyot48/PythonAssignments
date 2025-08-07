def sum_until_single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

num = int(input("Enter a number: "))

final_sum = sum_until_single_digit(num)
print("Final Output:", final_sum)
