def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def has_valid_differences(lst):
    return all(1 <= abs(a-b) < 4 for a, b in zip(lst, lst[1:]))

def is_safe(lst):
    return is_sorted(lst) and has_valid_differences(lst)

def can_be_safe_by_removal(lst):
    for i in range(len(lst)):
        modified_list = lst[:i] + lst[i+1:]
        if is_safe(modified_list):
            return True
    return False

def safe_data_check(raw_data):
    check_list = [list(map(int, line.split())) for line in raw_data.splitlines()]

    safe_report=0
    for lst in check_list:
        if is_safe(lst) or can_be_safe_by_removal(lst):
            safe_report += 1
    return safe_report


if __name__ == "__main__":
    with open('raw_data2.txt', 'r') as file:
        raw_data = file.read()
    result = safe_data_check(raw_data)
    print(result)

