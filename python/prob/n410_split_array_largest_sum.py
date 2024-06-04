from typing import List

def splitArray(self, nums: List[int], m: int) -> int:

    def check(target):
        groups = 0
        current_sum = 0
        for i in nums:
            current_sum += i
            if current_sum > target:
                groups += 1
                if groups >= m:
                    return False
                current_sum = i
        return True

    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = l + (r - l) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l
