class LetterCombination:
    map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }


    def letterCombination(self, digits: str) -> List[str]:
        if not digits:
            return []

        results = []
        self.helper(digits, 0, [], results)
        return results

    def helper(self, digits, level, chars, res):
        if level == len(digits):
            res.append(''.join(chars))
            return

        for letter in self.map[digits[level]]:
            chars.append(letter)
            self.helper(digits, level + 1, chars, res)
            chars.pop()
