class GenerateParenthese:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, n, "", res)
        return res 

    def dfs(self, left, right, n, cur, res):
        if left > n or right > n:
            return
        if left < right:
            return
        if left == n and right == n:
            res.append(cur)

        self.dfs(left + 1, right, n, cur + '(', res)
        self.dfs(left, right + 1, n, cur + ')', res)
