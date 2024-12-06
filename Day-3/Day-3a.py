import re
def find_uncorrupted(raw_data):
    pattern = r"mul\((\d+),(\d+)\)"
    total_prod = 0
    for line in raw_data.splitlines():
        matches = re.findall(pattern, line)

        for match in matches:
            num1, num2 = map(int, match)
            prod = (num1 * num2)
            total_prod += prod
    return total_prod

if __name__ == "__main__":
    with open('raw_data3.txt', 'r') as file:
        raw_data = file.read()
    result = find_uncorrupted(raw_data)
    print(result)