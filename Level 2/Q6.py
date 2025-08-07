def is_power_of_two(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)
num = int(input("Enter a number: "))
print("Is power of two?", is_power_of_two(num))
