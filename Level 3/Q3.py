# Q3: Replace all 'J' with 'I' and display content

def JtoI():
    file_path = "/Users/prajyotdhotre/Desktop/Excersise/PythonAssignments/Level 3/Lorem_Ipsum_Test_Data.txt"
    
    with open(file_path, "r") as file:
        content = file.read()
        corrected = content.replace('J', 'I')
        print("Corrected Content:\n", corrected)

JtoI()
