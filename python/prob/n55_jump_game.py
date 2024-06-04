from typing import List


class JumpGame:

    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        n = len(nums)
        for i in range(n):
            if i > reach or reach > n - 1:
                break
            reach = max(reach, i + nums[i])
        return reach >= n - 1
