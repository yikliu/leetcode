'''
List comprehension examples
'''
def addOneAndTwo(self, nums, n):
    return [nums[i] + 1 if i % 2 == 1 else nums[i] + 2 for i in range(n)]
