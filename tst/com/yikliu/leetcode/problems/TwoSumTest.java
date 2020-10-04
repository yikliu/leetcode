package com.yikliu.leetcode.problems;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class TwoSumTest {

    private TwoSum twoSum;

    @BeforeClass
    public void setup() {
        twoSum = new TwoSum();
    }

    @Test
    public void testTwoSum() {

        int[] result = twoSum.twoSum(new int[] { 2, 7, 11, 15 }, 9);
        Assert.assertEquals(result, new int[] { 0, 1 });

        result = twoSum.twoSum(new int[]{3, 2, 4}, 6);
        Assert.assertEquals(result, new int[] {1, 2});

        result = twoSum.twoSum(new int[]{3, 3}, 6);
        Assert.assertEquals(result, new int[] {0, 1});
    }
}
