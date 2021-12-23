class LongestPalindromicSubString:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        mx = [[False] * n for _ in range(n)]

        for i in range(n):
            mx[i][i] = True

        for i in range(1, n):
            mx[i][i - 1] = True

        longest, start, end = -1, 0, 0
        for dist in range(1, n):
            for i in range(n - dist):
                j = i + dist
                mx[i][j] = s[i] == s[j] and mx[i+1][j-1]
                if mx[i][j] and dist + 1 > longest:
                    longest = dist + 1
                    start, end = i, j

        return s[start:end + 1]
