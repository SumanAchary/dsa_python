def binary_search(arr, k):
    left = 0
    right = len(arr)
    found = False

    while left < right:
        mid = (left + right) // 2
        if k == arr[mid]:
            print(f"The item {k} is at the index {mid}")
            found = True
            break
        elif k < arr[mid]:
            right = mid
        else:
            left = mid + 1

    if not found:
        print("NOT FOUND")

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 78, 999, 4321, 432467, 43249]
    binary_search(arr, 999)
