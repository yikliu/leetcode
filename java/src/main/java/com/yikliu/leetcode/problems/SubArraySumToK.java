package com.yikliu.leetcode.problems;

import java.util.HashMap;
import java.util.Map;

/**
 * Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [1,1,1], k = 2
 * Output: 2
 *
 * Example 2:
 *
 * Input: nums = [1,2,3], k = 3
 * Output: 2
 */
public class SubArraySumToK {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int sum = 0;
        int ans = 0;
        for (int num : nums) {
            sum += num;
            if (map.containsKey(sum - k))
                ans += map.get(sum - k);
            map.merge(sum, 1, Integer::sum);
        }
        return ans;
    }
}
