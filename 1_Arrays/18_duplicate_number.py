def remove_duplicate(arr):
    seen_hash = dict()
    new_arr = []
    for ele in arr:
        if ele not in seen_hash:
            seen_hash[ele] = 1
            new_arr.append(ele)
    return new_arr


my_list = [1, 1, 2, 2, 3, 4, 5]

print(remove_duplicate(my_list))
