def check_similarity_score(raw_data):
    # Split raw data into two lists
    list1, list2 = [], []
    for line in raw_data.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    # Calculating Similarity Score
    similarity_score=0
    for i in list1:
        count=0
        for j in list2:
            if i==j:
                count+=1
        similarity_score += i*count
    return similarity_score

if __name__ == "__main__":
    with open('raw_data1.txt', 'r') as file:
        raw_data = file.read()
    result = check_similarity_score(raw_data)
    print(result)
