# Creating a list
my_list = [1, 2, 3, 4, 5]

# Appending an element to the end of the list
my_list.append(6)
# Result: [1, 2, 3, 4, 5, 6]

# Extending the list with another list
my_list.extend([7, 8, 9])
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inserting an element at a specific index
my_list.insert(2, 10)
# Result: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# Removing the last element and returning it
popped_item = my_list.pop()
# Result: popped_item = 9, my_list = [1, 2, 10, 3, 4, 5, 6, 7, 8]

# Removing a specific element by value
my_list.remove(3)
# Result: [1, 2, 10, 4, 5, 6, 7, 8]

# Finding the index of an element
index = my_list.index(4)
# Result: index = 3

# Counting the occurrences of an element
count = my_list.count(4)
# Result: count = 1

# Reversing the list in-place
my_list.reverse()
# Result: [8, 7, 6, 5, 4, 10, 2, 1]

# Sorting the list in-place (ascending order)
my_list.sort()
# Result: [1, 2, 4, 5, 6, 7, 8, 10]

# Sorting the list in-place (descending order)
my_list.sort(reverse=True)
# Result: [10, 8, 7, 6, 5, 4, 2, 1]

# Copying the list (shallow copy)
new_list = my_list.copy()
# Result: new_list = [10, 8, 7, 6, 5, 4, 2, 1]

# Clearing all elements from the list
my_list.clear()
# Result: []

# Checking if an element is in the list
element_in_list = 5 in new_list
# Result: element_in_list = True

# Getting the length of the list
list_length = len(new_list)
# Result: list_length = 8
