def print_pairs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"{arr[i]}-{arr[j]}")

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60]
    print_pairs(arr)
