package leetcode

func isValidParentheses(s string) bool {
	stk := make(stack, 0)
	mapping := map[rune]rune{
		'{': '}',
		'[': ']',
		'(': ')'}

	for _, ch := range s {
		switch ch {
		case '{', '[', '(':
			stk = stk.push(ch)
			break
		case '}', ']', ')':
			var rn rune
			if stk.empty() {
				return false
			}
			stk, rn = stk.pop()
			if ch != mapping[rn] {
				return false
			}
		}
	}
	return stk.empty()
}

type stack []rune

func (s stack) push(v rune) stack {
	return append(s, v)
}

func (s stack) pop() (stack, rune) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func (s stack) empty() bool {
	return len(s) == 0
}
