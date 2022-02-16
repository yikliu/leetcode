class MaxSubArray:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        mx = [nums[0]]
        max = nums[0]
        for i in range(1, n):
            if mx[i-1] + nums[i] > nums[i]:
                mx.append(mx[i-1] + nums[i])
            else:
                mx.append(nums[i])
            if max < mx[i]:
                max = mx[i]
        return max
