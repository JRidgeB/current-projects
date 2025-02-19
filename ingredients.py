import math

def read_file_to_arrays(filename):
    with open(filename, 'r') as file:
        # Read the first two lines as integers
        first_line = int(file.readline().strip())
        second_line = int(file.readline().strip())

        # Initialize arrays to store the data
        array1 = []
        array2 = []
        array3 = []

        # Loop through the rest of the file
        for line in file:
            # Split each line into 3 variables
            parts = line.strip().split()
            var1 = parts[0]       # First variable as a string
            var2 = int(parts[1])  # Second variable as an integer
            var3 = parts[2]       # Third variable as a string

            # Append the variables to their respective arrays
            array1.append(var1)
            array2.append(var2)
            array3.append(var3)
        mult = math.ceil(second_line/first_line)
        for i in range(len(array2)):
            amount = array2[i]  
            amount = amount * mult  
            array2[i] = amount  


    return first_line, second_line, array1, array2, array3

def print_ingredients(array1, array2, array3):
    print("ingredient, amount, measurement")
    for i in range(len(array1)):
        print(array1[i]," ",array2[i]," ",array3[i])
        
        print()  # Add a blank line for readability

# Example usage
filename = 'example.txt'
first_line, second_line, array1, array2, array3 = read_file_to_arrays(filename)
print("Original Recipe serving:", first_line)
print("Amount of expected people:", second_line)
print_ingredients(array1, array2, array3)
