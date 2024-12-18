def page_number():
    rules = []
    orders = []
    with open("raw_data5.txt") as file:
        for line in file.readlines():
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            if ',' in line:
                orders.append(list(map(int, line.split(','))))

    valid_orders = []
    sum_of_middles = 0

    for order in orders:
        is_valid = True
        for first, second in rules:
            if first not in order or second not in order:
                continue

            if order.index(first) > order.index(second):
                is_valid = False

        if is_valid:
            valid_orders.append(order)
    
    sum_of_middles = 0
    for valid_order in valid_orders:
        sum_of_middles += valid_order[len(valid_order)//2]

    return sum_of_middles
        
print(page_number())