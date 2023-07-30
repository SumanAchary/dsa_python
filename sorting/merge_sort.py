def merge_sort(arr):
    """
    Merge Sort Algorithm:
    - Divide the input array into two halves
    - Recursively sort each half
    - Merge the two sorted halves back into a single sorted array

    :param arr: The input array to be sorted
    :return: The sorted array
    """

    # Base case: If the array has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half (Divide & Conquer)
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.

    :param left: The left sorted array
    :param right: The right sorted array
    :return: The merged sorted array
    """
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both arrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left array
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add any remaining elements from the right array
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
