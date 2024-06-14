def count_chars(string):
    count = {}
    for char in string:
        count[char] = count.get(char,0) + 1
    return count
string = input("Nhập xâu ký tự : ")
print(count_chars(string))