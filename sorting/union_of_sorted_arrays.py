# Naive Approach
def union_of_sorted_arrays_naive(arr1, arr2):
    arr3 = sorted(set(arr1 + arr2))
    print(" ".join(str(num) for num in arr3))


def union_of_sorted_arrays_optimal(arr1, arr2):
    i = 0
    j = 0
    arr1_len = len(arr1)
    arr2_len = len(arr2)

    while i < arr1_len and j < arr2_len:
        if arr1[i] < arr2[j]:
            if arr1[i] != arr1[i - 1]:
                print(arr1[i], end=" ")
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != arr2[j - 1]:
                print(arr2[j], end=" ")
            j += 1
        else:  # Both elements are equal
            print(arr1[i], end=" ")
            i += 1
            j += 1

    # Add remaining elements from arr1 (if any)
    while i < arr1_len:
        if i == 0 or arr1[i] != arr1[i - 1]:
            print(arr1[i], end=" ")
        i += 1

    # Add remaining elements from arr2 (if any)
    while j < arr2_len:
        if j == 0 or arr2[j] != arr2[j - 1]:
            print(arr2[j], end=" ")
        j += 1


union_of_sorted_arrays_naive([1, 2, 3, 4, 4, 4, 5], [2, 3, 5, 7, 8, 9])
union_of_sorted_arrays_optimal([1, 2, 3, 4, 4, 4, 5], [2, 3, 5, 7, 8, 9])
