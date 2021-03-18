package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 *
 * Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
 *
 * The order of output does not matter.
 *
 * Example 1:
 *
 * Input:
 * s: "cbaebabacd" p: "abc"
 *
 * Output:
 * [0, 6]
 *
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of "abc".
 *
 *
 *
 * Example 2:
 *
 * Input:
 * s: "abab" p: "ab"
 *
 * Output:
 * [0, 1, 2]
 *
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 */
public class FindAllAnagrams {
    public List<Integer> findAnagrams(String s, String p) {
        //sliding windows, two maps
        int sp = p.length();
        List<Integer> ans = new ArrayList<>();
        Map<Character, Integer> pCount = new HashMap<>();
        for (char c : p.toCharArray()) {
            pCount.merge(c, 1, Integer::sum);
        }
        Map<Character, Integer> windowCount = new HashMap<>();
        for (int i = 0; i < sp; i++) {
            windowCount.merge(s.charAt(i), 1, Integer::sum);
        }
        if (pCount.equals(windowCount)) {
            ans.add(0);
        }

        int j = 1; int k = sp;
        while(k < s.length()) {
            if (!pCount.containsKey(s.charAt(k))) {
                j = k + 1;
                k = j + sp - 1;
                continue;
            }
            windowCount.merge(s.charAt(j - 1), 1, Integer::compare);
            windowCount.merge(s.charAt(k), 1, Integer::sum);
            if (pCount.equals(windowCount)) {
                ans.add(j);
            }
            j++;
            k++;
        }

        return ans;
    }
}
