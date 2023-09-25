def print_sub_arrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=",")
            print()


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print_sub_arrays(arr)
