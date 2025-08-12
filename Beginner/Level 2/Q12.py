username = input("Enter username: ")
password = input("Enter password: ")
retype = input("Re-type password: ")

attempts = 1

while password != retype and attempts < 3:
    print("Passwords do not match. Try again.")
    retype = input("Re-type password: ")
    attempts += 1

if password == retype:
    print("Login successful!")
else:
    print("Too many failed attempts. Try again later.")
