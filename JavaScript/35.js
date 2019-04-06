/*
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

* @param {number[]} nums
* @param {number} target
* @return {number}
*/

var searchInsert = function(nums, target) {
    // 1
    let left = 0, right = nums.length - 1;
    while (left <= right) {
        mid = left + Math.floor((right - left) / 2);
        if (nums[mid] > target) {
            right = mid - 1;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            return mid;
        }
    }
    return left;
};