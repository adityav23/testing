import time

"""
Function: fibonacci
Description: Generates the Fibonacci sequence up to n terms.
Input: 
    n (int): The number of terms in the Fibonacci sequence to generate.
Output: 
    list: A list containing the Fibonacci sequence up to n terms.
Algorithm: 
    1. Initialize the first two terms of the Fibonacci sequence [0, 1].
    2. Iterate from the 2nd term to the nth term.
    3. For each term, append the sum of the previous two terms to the sequence.
    4. Return the Fibonacci sequence list.
"""
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        # Append the sum of the last two terms to the sequence
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq


"""
Function: factorial
Description: Recursively calculates the factorial of a number.
Input: 
    n (int): The number for which the factorial is to be calculated.
Output: 
    int: The factorial of the input number.
Algorithm: 
    1. If n is 0 or 1, return 1 (base case).
    2. Otherwise, recursively call the factorial function with n-1 and multiply the result with n.
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


"""
Function: matrix_multiply
Description: Multiplies two matrices and returns the result.
Input: 
    matrix1 (list of lists): The first matrix.
    matrix2 (list of lists): The second matrix.
Output: 
    list of lists: The resulting matrix after multiplication.
Algorithm: 
    1. Initialize an empty result matrix with dimensions matching matrix1 and matrix2.
    2. Iterate through rows of matrix1 and columns of matrix2.
    3. For each element in the result matrix, calculate the dot product of the corresponding row and column.
    4. Return the resulting matrix.
"""
def matrix_multiply(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Iterate through rows of matrix1
    for i in range(len(matrix1)):
        # Iterate through columns of matrix2
        for j in range(len(matrix2[0])):
            # Iterate through rows of matrix2
            for k in range(len(matrix2)):
                # Multiply and accumulate the product for result[i][j]
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


"""
Function: write_to_file
Description: Writes data to a file.
Input: 
    filename (str): The name of the file to write to.
    data (str): The data to be written to the file.
Output: 
    None
Algorithm: 
    1. Open the file in write mode.
    2. Write the provided data to the file.
    3. Close the file.
"""
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        # Write the provided data to the file
        file.write(data)


"""
Function: read_from_file
Description: Reads data from a file.
Input: 
    filename (str): The name of the file to read from.
Output: 
    str: The data read from the file.
Algorithm: 
    1. Open the file in read mode.
    2. Read the content of the file.
    3. Return the content as a string.
"""
def read_from_file(filename):
    with open(filename, 'r') as file:
        # Read and return the file content
        return file.read()


"""
Function: run_tests
Description: Runs a series of tests, including generating the Fibonacci sequence, calculating factorial, 
             performing matrix multiplication, writing to a file, and reading from a file.
Input: 
    None
Output: 
    None
Algorithm: 
    1. Generate the Fibonacci sequence for a given number of terms and print the result.
    2. Calculate the factorial of a number and print the result.
    3. Perform matrix multiplication on two 3x3 matrices and print the result.
    4. Write the generated Fibonacci sequence to a file and print the time taken.
    5. Read the Fibonacci sequence from the file and print the read data.
"""
def run_tests():
    # Fibonacci test
    print("Generating Fibonacci sequence...")
    n = 35  # Increase this number for a longer sequence
    start_time = time.time()
    fib_seq = fibonacci(n)
    print(f"Fibonacci sequence up to {n} terms:\n", fib_seq)
    print(f"Time taken for Fibonacci: {time.time() - start_time:.5f} seconds\n")

    # Factorial test
    print("Calculating Factorial...")
    number = 20  # Increase this number to test recursion
    start_time = time.time()
    fact_result = factorial(number)
    print(f"Factorial of {number}: {fact_result}")
    print(f"Time taken for Factorial: {time.time() - start_time:.5f} seconds\n")

    # Matrix multiplication test
    print("Performing Matrix Multiplication...")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    start_time = time.time()
    result_matrix = matrix_multiply(matrix1, matrix2)
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
    print(f"Time taken for Matrix Multiplication: {time.time() - start_time:.5f} seconds\n")

    # File writing test
    print("Writing Fibonacci sequence to a file...")
    start_time = time.time()
    fib_data = ", ".join(map(str, fib_seq))
    write_to_file("fibonacci.txt", fib_data)
    print(f"Fibonacci sequence written to 'fibonacci.txt' in {time.time() - start_time:.5f} seconds\n")

    # File reading test
    print("Reading Fibonacci sequence from the file...")
    start_time = time.time()
    fib_data_from_file = read_from_file("fibonacci.txt")
    print(f"Data read from 'fibonacci.txt':\n{fib_data_from_file}")
    print(f"Time taken for file read: {time.time() - start_time:.5f} seconds\n")


if __name__ == "__main__":
    run_tests()
