package com.yikliu.leetcode.problems;

import java.util.Collections;

/**
 * Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
 *
 * If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
 *
 * The replacement must be in-place and use only constant extra memory.
 *
 * Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
 *
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 *
 *
 *
 * 这道题让我们求下一个排列顺序，由题目中给的例子可以看出来，如果给定数组是降序，则说明是全排列的最后一种情况，则下一个排列就是最初始情况，可以参见之前的博客 Permutations。再来看下面一个例子，有如下的一个数组
 *
 * 1　　2　　7　　4　　3　　1
 *
 * 下一个排列为：
 *
 * 1　　3　　1　　2　　4　　7
 *
 * 那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，然后再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：
 *
 * 1　　2　　7　　4　　3　　1
 *
 * 1　　2　　7　　4　　3　　1
 *
 * 1　　3　　7　　4　　2　　1
 *
 * 1　　3　　1　　2　　4　　7
 */
public class NextPermutation {
    public void nextPermutation(int[] nums) {
        for (int i = nums.length - 2; i > 0; i--) {
            if (nums[i + 1] > nums[i]) {
                int j = nums.length - 1;
                for (; j > i; j--) {
                    if (nums[j] > nums[i]) {
                        break;
                    }
                }
                swap(nums, i, j);
                reverse(nums, i + 1, nums.length - 1);
                return;
            }
        }
        reverse(nums, 0, nums.length - 1);
    }

    private void swap(int[] list, int i, int j) {

    }

    private void reverse(int[] list, int i, int j) {

    }
}
