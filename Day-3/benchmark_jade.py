import re
import timeit

def part1():
    lines = []
    with open("raw_data3.txt") as file:
        lines = file.readlines()

    total = 0

    for line in lines:
        multiplications = re.findall("mul\(\d{1,3},\d{1,3}\)", line)

        for multiplication in multiplications:
            numbers = list(map(int, re.findall("\d+", multiplication)))
            total += numbers[0] * numbers[1]

    return total

def benchmark():
    part1()

# Benchmark the function
execution_time = timeit.timeit(benchmark, number=100)
print(f"Average Execution Time: {execution_time / 100:.6f} seconds")
