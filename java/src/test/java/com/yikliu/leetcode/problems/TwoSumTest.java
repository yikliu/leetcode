package com.yikliu.leetcode.problems;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TwoSumTest {

    private TwoSum twoSum;

    @BeforeEach
    public void setup() {
        twoSum = new TwoSum();
    }

    @Test
    public void testTwoSum() {

        int[] result = twoSum.twoSum(new int[] { 2, 7, 11, 15 }, 9);
        Assertions.assertArrayEquals(result, new int[] { 0, 1 });

        result = twoSum.twoSum(new int[]{3, 2, 4}, 6);
        Assertions.assertArrayEquals(result, new int[] {1, 2});

        result = twoSum.twoSum(new int[]{3, 3}, 6);
        Assertions.assertArrayEquals(result, new int[] {0, 1});
    }
}
