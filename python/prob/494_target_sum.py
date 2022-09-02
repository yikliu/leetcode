from typing import List
answer = 0
memo = {}

def findTargetSumWays(nums: List[int], target: int) -> int:
    dfs(nums, target, 0, 0)
    return answer

"""
This one is not trimmed and will time out
"""
def dfs(nums, target, cur, index):
    if index == len(nums) and cur == target:
        answer += 1
    elif index == len(nums):
        return
    elif memo[(cur, target - cur)]:
        return
    else:
        dfs(nums, target, cur + nums[index], index + 1)
        dfs(nums, target, cur - nums[index], index + 1)
    memo[(cur, target - cur)] = answer
