arr = [1, 2, 3, 4, 5, 6, 7, 8, 6, 43, 2, 555, 9]
max_value = max(arr)
print(max_value)

# Another approach!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 6, 43, 2, 555, 9]
max_value = float('-inf')  # Initialize max_value to negative infinity

for num in arr:
    if num > max_value:
        max_value = num

print(max_value)
