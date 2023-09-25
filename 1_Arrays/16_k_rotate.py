def k_rotate(arr, k):
    n = len(arr)
    k = k % n

    rotated = []

    for i in range(n - k, n):
        rotated.append(arr[i])

    for i in range(n - k):
        rotated.append(arr[i])

    return rotated


def k_rotate_optimised(arr, k):
    n = len(arr)
    rot_idx = n - k

    for i in range(rot_idx, n):
        arr.append(arr.pop(rot_idx))

    return arr


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    k = 2

    rotated = k_rotate(input_list, k)
    rotated_opt = k_rotate_optimised(input_list, k)

    print("Original list:", input_list)
    print("Rotated list:", rotated)
    print("Rotated list Optimized:", rotated_opt)
