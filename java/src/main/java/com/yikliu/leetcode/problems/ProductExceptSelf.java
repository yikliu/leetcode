package com.yikliu.leetcode.problems;

/**
 * Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
 *
 * Example:
 *
 * Input:  [1,2,3,4]
 * Output: [24,12,8,6]
 */
public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] fwd = new int[nums.length];
        fwd[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            fwd[i] = fwd[i - 1] * nums[i - 1];
        }
        int[] bwd = new int[nums.length];
        bwd[nums.length - 1] = 1;
        for (int j = nums.length - 2; j >= 0; j--) {
            bwd[j] = bwd[j + 1] * nums[j + 1];
        }
        int[] res = new int[nums.length];
        for (int k = 0; k < nums.length; k++) {
            res[k] = fwd[k] * bwd[k];
        }
        return res;
    }
}
