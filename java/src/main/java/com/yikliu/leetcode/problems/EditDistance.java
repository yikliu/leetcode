/**
 * https://leetcode.com/problems/edit-distance/
 * Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
 *
 * You have the following 3 operations permitted on a word:
 *
 * Insert a character
 * Delete a character
 * Replace a character
 * Example 1:
 *
 * Input: word1 = "horse", word2 = "ros"
 * Output: 3
 * Explanation:
 * horse -> rorse (replace 'h' with 'r')
 * rorse -> rose (remove 'r')
 * rose -> ros (remove 'e')
 * Example 2:
 *
 * Input: word1 = "intention", word2 = "execution"
 * Output: 5
 * Explanation:
 * intention -> inention (remove 't')
 * inention -> enention (replace 'i' with 'e')
 * enention -> exention (replace 'n' with 'x')
 * exention -> exection (replace 'n' with 'c')
 * exection -> execution (insert 'u')
 */

package com.yikliu.leetcode.problems;

public class EditDistance {
    int minEditDistance(final String s1, final String s2) {
        int n = s1.length();
        int m = s2.length();
        int[][] f = new int[n + 1][m + 1];

        for (int i = 0; i <= n; i++) {
            f[i][0] = i;
        }

        for (int j = 0; j <= m; j++) {
            f[0][j] = j;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    f[i][j] = f[i - 1][j - 1];
                } else {
                    int mn = Math.min(f[i - 1][j], f[i][j - 1]);
                    f[i][j] = Math.min(mn, f[i - 1][j - 1]) + 1;
                }
            }
        }
        return f[n][m];
    }
}
