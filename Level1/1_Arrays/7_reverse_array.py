def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    arr = ["S", "U", "M", "A", "N"]

    print("\nBEFORE REVERSED")
    for char in arr:
        print(char, end="")

    reverse_array(arr)

    print("\nAFTER REVERSED")
    for char in arr:
        print(char, end="")
