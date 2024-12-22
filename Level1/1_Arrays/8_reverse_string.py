def reverse_string(input_str):
    # Convert the input string to a list of characters
    arr = list(input_str)
    left, right = 0, len(arr) - 1  # Initialize left and right pointers

    while left < right:
        # Swap characters at left and right positions
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Join the characters back into a string
    return ''.join(arr)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)
