package com.yikliu.leetcode.problems;

import java.util.HashMap;

public class VerifyAlienDictionary {

    public boolean solve(String[] words, String order) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }

        for (int i = 1; i < words.length; i++) {
            String w1 = words[i - 1];
            String w2 = words[i];
            int j = 0;
            for (; j < w1.length() && j < w2.length(); j++) {
                if (w1.charAt(j) == w2.charAt(j)) continue;
                else if (map.get(w1.charAt(j)) > map.get(w2.charAt(j))) return false;
                else break;
            }
            if (j < w1.length() && j == w2.length()) return false;
        }

        return true;
    }

}
