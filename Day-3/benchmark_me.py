import re
import timeit

# Define the function to benchmark
def find_uncorrupted(raw_data):
    pattern = r"mul\((\d+),(\d+)\)"
    total_prod = 0
    for line in raw_data.splitlines():
        matches = re.findall(pattern, line)

        for match in matches:
            num1 = int(match[0])
            num2 = int(match[1])
            prod = (num1 * num2)
            total_prod += prod
    return total_prod

# Create a sample input dataset
with open('raw_data3.txt', 'r') as file:
        raw_data = file.read()

# Function wrapper for timeit
def benchmark():
    find_uncorrupted(raw_data)

# Benchmark using timeit
execution_time = timeit.timeit(benchmark, number=100)  # Run 100 iterations
print(f"Average Execution Time: {execution_time / 100:.6f} seconds")
