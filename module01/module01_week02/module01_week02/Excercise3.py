def word_count(data):
    data_lower = data.lower()
    data_list = data_lower.split()
    count = {}
    for word in data_list:
        count[word] = count.get(word,0) + 1
    return count

with open('module01_week02\module01_week02\P1_data.txt', 'r') as f2:
    data = f2.read()
    dict = word_count(data)
    print(dict)