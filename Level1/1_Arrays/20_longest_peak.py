def longestPeak(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        if is_peak(array, i):

            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1

            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1

            current_peak = rightIdx - leftIdx - 1
            longest_peak_length = max(longest_peak_length, current_peak)
            i = rightIdx
        else:
            i += 1
    return longest_peak_length


def is_peak(arr, current_idx):
    prev = arr[current_idx - 1]
    next = arr[current_idx + 1]
    return prev < arr[current_idx] > next
