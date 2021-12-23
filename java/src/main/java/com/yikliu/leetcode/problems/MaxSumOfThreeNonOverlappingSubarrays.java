package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.List;

/**
 * In a given array nums of positive integers, find three non-overlapping sub-arrays with maximum sum.
 *
 * Each sub-array will be of size k, and we want to maximize the sum of all 3*k entries.
 *
 * Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
 *
 * Example:
 *
 * Input: [1,2,1,2,6,7,5,1], 2
 * Output: [0, 3, 5]
 * Explanation: Sub-arrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
 * We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 *
 *
 *
 * Note:
 *
 *     nums.length will be between 1 and 20000.
 *     nums[i] will be between 1 and 65535.
 *     k will be between 1 and floor(nums.length / 3).
 *
 */

/** NOT FINISHED **/
public class MaxSumOfThreeNonOverlappingSubarrays {
    int[] maxSumOfThreeSubarrays (int[] nums, int k) {
        int[] sums = new int[nums.length];
        sums[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sums[i] = sums[i - 1] + nums[i];
        }
        int max_left = sums[k] - sums[0];
        List<Integer> lefts = new ArrayList<>();
        for (int i = k; i < nums.length; i++) {
            int sumK = sums[i + 1] - sums[i + 1 - k];
            if (sumK > max_left) {
                lefts.add(i + 1);
            } else {
                lefts.add(lefts.get(i - 1));
            }
        }
        return sums;
    }
}
