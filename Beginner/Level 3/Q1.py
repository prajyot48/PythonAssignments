def get_even_length_words():
    file_path = "/Users/prajyotdhotre/Desktop/Excersise/PythonAssignments/Level 3/Lorem_Ipsum_Test_Data.txt"
    
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()
        even_words = [word for word in words if len(word) % 2 == 0]
        
        print("Even-length words:")
        print(" ".join(even_words))

get_even_length_words()
