def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


if __name__ == "__main__":
    arr = [1, 34, 1234, 6754, 23, 4, 12, 3, 5, 8]
    k = 0
    found = linear_search(arr, k)
    if found != -1:
        print(f"The element {k} has been found at the index {found}")
    else:
        print("Damn! No such items found in the array")
