from typing import List

def generateParenthesis(n: int) -> List[str]:
    res = []
    dfs(0, 0, n, "", res)
    return res

def dfs(left, right, n, cur, res):
    if left > n or right > n:
        return
    if left < right:
        return
    if left == n and right == n:
        res.append(cur)

    dfs(left + 1, right, n, cur + '(', res)
    dfs(left, right + 1, n, cur + ')', res)
