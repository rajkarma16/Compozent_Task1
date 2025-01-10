#Create a script to read a text file, count the number of words, and write the results to a new file.
input_file = (r'Task 1 Python\FIle_Handling\input.txt')
output_file = (r'Task 1 Python\FIle_Handling\output.txt')

try:
    a = open(input_file,'r')
    b = a.read() 
    count = len(b.split())  #splitting contents of input file and counting
    
    d = open(output_file, 'w')
    d.write(f"The number of words in {input_file} is : {count}")

    print("Operation Successful")
except FileNotFoundError:
    print(f"{input_file} not found")
except Exception as e:
    print(f"Unexpected error occurred : {e}")