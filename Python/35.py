'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

def searchInsert(self, nums: List[int], target: int) -> int:
    # 1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


    # 2
    return len([x for x in nums if x<target])

    # 3
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return left