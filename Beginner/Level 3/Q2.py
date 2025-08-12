def count_lines():
    file_path = "/Users/prajyotdhotre/Desktop/Excersise/PythonAssignments/Level 3/Lorem_Ipsum_Test_Data.txt"
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

count_lines()
