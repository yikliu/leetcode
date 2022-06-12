class TargetSum:
    answer = 0
    memo = {}

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dfs(nums, target, 0, 0)
        return self.answer

    """
    This one is not trimmed and will time out
    """
    def dfs(self, nums, target, cur, index):
        if index == len(nums) and cur == target:
            self.answer += 1
        elif index == len(nums):
            return
        elif self.memo[(cur, target - cur)]:
            return
        else:
            self.dfs(nums, target, cur + nums[index], index + 1)
            self.dfs(nums, target, cur - nums[index], index + 1)
        self.memo[(cur, target - cur)] = self.answer
