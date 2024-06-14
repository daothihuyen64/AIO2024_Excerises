def sliding_window(num_list, k):
    result_list = []
    start_id = 0
    end_id = k-1
    while (end_id != len(num_list)):
        slide_k = num_list[start_id: end_id + 1]
        result_list.append(max(slide_k))
        start_id += 1
        end_id += 1
    return result_list


n = int(input("hãy nhập số phần tử của mảng"))
num_list = [int(input()) for _ in range(n)]
k = int(input())
print(sliding_window(num_list, k))
