# Approach 1: Brute Force
def max_subarray_sum1(arr):
    n = len(arr)
    largest_sum = float("-inf")  # Initialize with negative infinity

    for i in range(n):
        for j in range(i, n):
            sub_array_sum = sum(arr[i : j + 1])
            largest_sum = max(largest_sum, sub_array_sum)

    return largest_sum


# Approach 2: Prefix Sum
def max_subarray_sum2(arr):
    n = len(arr)
    largest_sum = float("-inf")
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    for i in range(n):
        for j in range(i, n):
            sub_array_sum = prefix_sum[j] - (prefix_sum[i - 1] if i > 0 else 0)
            largest_sum = max(largest_sum, sub_array_sum)

    return largest_sum


# Approach 3: Kadane's Algorithm
def max_subarray_sum3(arr):
    n = len(arr)
    largest_sum = float("-inf")
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        largest_sum = max(current_sum, largest_sum)
        if current_sum < 0:
            current_sum = 0

    return largest_sum


if __name__ == "__main__":
    arr = [-2, 3, 4, -1, 5, -12, 6, 1, 3]

    # Approach 1
    result1 = max_subarray_sum1(arr)
    print(result1)

    # Approach 2
    result2 = max_subarray_sum2(arr)
    print(result2)

    # Approach 3
    result3 = max_subarray_sum3(arr)
    print(result3)
