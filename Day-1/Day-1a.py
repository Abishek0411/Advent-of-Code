# Function to find distance
def total_absolute_difference_from_raw(raw_data):
    # Split raw data into two lists
    list1, list2 = [], []
    for line in raw_data.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    
    # Sorting Lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    # Calculating Distance
    total_difference = sum(abs(a - b) for a, b in zip(sorted_list1, sorted_list2))
    return total_difference

if __name__ == "__main__":
    # Read raw data from the text file
    with open('raw_data1.txt', 'r') as file:
        raw_data = file.read()
    

    result = total_absolute_difference_from_raw(raw_data)
    print("Total Absolute Difference:", result)

