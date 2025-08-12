string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if sorted(string1.lower()) == sorted(string2.lower()):
    print("True")
else:
    print("False")
