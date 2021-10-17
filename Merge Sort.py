import random

def sort(nums):
    left, right = nums[:len(nums)//2], nums[len(nums)//2:]
    if len(left) > 1:
        left = sort(left)
    if len(right) > 1:
        right = sort(right)
    i = 0
    while left and right:
        nums[i] = left.pop(0) if left[0] < right[0] else right.pop(0)
        i += 1
    if left:
        nums[-(len(left)):] = left
    elif right:
        nums[-(len(right)):] = right
    
    return nums

nums = [random.randint(0,100) for _ in range(10)]
print(nums)
print(sort(nums))