def safe_data_check(raw_data):
    check_list = []
    for line in raw_data.splitlines():
        split_list = []
        for element in line.split():
            int_num = int(element)
            split_list.append(int_num)
        check_list.append(split_list)

    safe_report = 0
    for i in check_list:    
        if i == sorted(i) or i == sorted(i, reverse=True):
            all_pairs_valid = True
            for a, b in zip(i,i[1:]):
                val = abs(a-b)
                if not (1<=val<4):
                    all_pairs_valid = False
                
            if all_pairs_valid:
                safe_report+=1        

    return safe_report


if __name__ == "__main__":    
    with open ('raw_data2.txt', 'r') as file:
        raw_data = file.read()
            
    result = safe_data_check(raw_data)
    print(result)