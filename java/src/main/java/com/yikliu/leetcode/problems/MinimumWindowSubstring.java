package com.yikliu.leetcode.problems;

import java.util.HashMap;
import java.util.Map;

/**
 * Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
 *
 * Example:
 *
 * Input: S = "ADOBECODEBANC", T = "ABC"
 * Output: "BANC"
 * Note:
 *
 * If there is no such window in S that covers all characters in T, return the empty string "".
 * If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
 */
public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        Map<Character, Integer> count = new HashMap<>();
        int left = 0;
        int right = 0;

        for (int i = 0; i < t.length(); i++) {
            count.merge(t.charAt(i), 1, Integer::sum);
        }
        Map<Character, Integer> run = new HashMap<>();
        while(left < right && right < s.length()) {
            Character atRight = s.charAt(right);
            if (count.containsKey(atRight)) {
                if (run.getOrDefault(atRight, 0) < count.get(atRight)) {
                    run.merge(atRight, 1, Integer::sum);
                    right++;
                } else {
                    left++;
                }
                //check is done; break;
            } else {
                right++;
            }
        }
        return s.substring(left, right + 1);
    }
}
