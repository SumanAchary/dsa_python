def contains_duplicate(nums):
    # TODO
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return True
 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 98, 4, 1]
print(contains_duplicate(nums))
