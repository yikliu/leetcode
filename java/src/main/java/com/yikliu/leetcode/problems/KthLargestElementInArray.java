package com.yikliu.leetcode.problems;

import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
 *
 * Example 1:
 *
 * Input: [3,2,1,5,6,4] and k = 2
 * Output: 5
 *
 * Example 2:
 *
 * Input: [3,2,3,1,2,4,5,5,6] and k = 4
 * Output: 4
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 */
public class KthLargestElementInArray {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<Integer>();
        List list = Arrays.asList(nums);
        q.addAll(list);
        for (int i = 0; i < nums.length - k; i++) {
            q.poll();
        }
        return q.peek();
    }
}
