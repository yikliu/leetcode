package com.yikliu.leetcode.problems;

/**
 * Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
 *
 * Example 1:
 *
 * **Input:** "aba"
 * **Output:** True
 * Example 2:
 *
 * **Input:** "abca"
 * **Output:** True
 * **Explanation:** You could delete the character 'c'.
 * Note:
 *
 * 1. The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
 */
public class ValidPalindromeII {

    public boolean validPalindrome(String s) {
        int begin = 0;
        int end = s.length() - 1;
        while (begin < end) {
            if (s.charAt(begin) != s.charAt(end)) {
                return isValidPalindrome(s, begin + 1, end)
                    || isValidPalindrome(s, begin, end - 1);
            }
            begin++;
            end--;
        }
        return true;
    }

    private boolean isValidPalindrome(String s, int left, int right) {
        while(left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
