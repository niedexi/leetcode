'''
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # RUNTIME(ms): 40
        lookup = {}
        for i , num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        

        # RUNTIME(ms): 56
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup[target - nums[i]], i]
            lookup[nums[i]] = i


        # RUNTIME(ms): 916
        for i in range(len(nums)):
            j = target - nums[i]
            temp_nums = nums[(i + 1):]
            if j in temp_nums:
                return [i, (temp_nums.index(j) + i + 1)]


        # RUNTIME(ms): 1316
        for i in nums:
            j = target - i
            tmp_nums_start_index = nums.index(i) + 1
            tmp_nums = nums[tmp_nums_start_index:]
            if j in tmp_nums:
                return [nums.index(i), tmp_nums_start_index + tmp_nums.index(j)]