'''
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.
'''


def minSortedArray(nums: List[int]) ->int:
    n = len(nums)
    l = 0
    r = n - 1
    if nums[r] > nums[0]:
        return nums[0]
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[mid] > nums[0]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
