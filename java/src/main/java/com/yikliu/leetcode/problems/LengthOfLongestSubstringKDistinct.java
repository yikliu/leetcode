package com.yikliu.leetcode.problems;

import java.util.HashMap;
import java.util.Map;

/**
 * Given a string, find the length of the longest substring T that contains at most k distinct characters.
 *
 * For example, Given s = “eceba” and k = 2,
 *
 * T is "ece" which its length is 3.
 *
 *
 */
public class LengthOfLongestSubstringKDistinct {

    public int lengthOfLongestSubstringKDistinct(String s, int k) {
       Map<Character, Integer> map = new HashMap<>();
       int left = 0;
       int ans = -1;
       for (int i = 0; i < s.length(); i++) {
           map.put(s.charAt(i), i);
           while (map.size() > k) {
               if (map.get(s.charAt(left)) == left) {
                   map.remove(s.charAt(left));
               }
               left++;
           }
           ans = Math.max(ans, i - left + 1);
       }
       return ans;
    }
}
