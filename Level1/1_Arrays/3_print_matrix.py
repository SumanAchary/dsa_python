def print_matrix(arr):
    for row in arr:
        for element in row:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    arr = [[1, 23, 4], [3, 3, 411]]
    print_matrix(arr)
