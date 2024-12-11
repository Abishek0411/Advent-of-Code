import re

def find_uncorrupted():
    lines = []
    with open("raw_data3.txt") as file:
        lines = file.readlines()

    total = 0
    can_do = True

    for line in lines:
        instructions = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", line)

        for instruction in instructions:
            # Check if the instruction is a 'do()' or 'don't()' string
            if instruction == 'do()':
                can_do = True
                continue  # Skip to next instruction

            if instruction == "don't()":
                can_do = False
                continue  # Skip to next instruction

            # If not 'do()' or 'don't()', it's a 'mul()' instruction
            if can_do:
                numbers = list(map(int, re.findall("\d+", instruction)))
                total += numbers[0] * numbers[1]

    return total

if __name__ == "__main__":
    print(str(find_uncorrupted()))
