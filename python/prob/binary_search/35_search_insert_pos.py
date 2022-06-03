'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

Challenge
O(log(n)) time
'''

def searchInRotation(A: List[int], target: int) -> int:
    n = len(A)
    l = 0
    r = n - 1

    while l + 1 < r:
        mid = l + (r - l) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid
        else:
            r = mid

    if A[l] >= target:
        return l
    elif A[r] >= target:
        return r
    else:
        return r + 1
