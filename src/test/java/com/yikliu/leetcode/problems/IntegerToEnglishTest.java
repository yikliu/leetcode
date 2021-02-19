package com.yikliu.leetcode.problems;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class IntegerToEnglishTest {

    private final IntegerToEnglish integerToEnglish = new IntegerToEnglish();

    @Test
    public void test2() {
        String expected = "One Thousand";
        String output = integerToEnglish.solve(1000);
        Assertions.assertEquals(output, expected);
    }

    @Test
    public void test() {
        String expected = "Twelve Thousand Three Hundred Forty Five";
        String output = integerToEnglish.solve(12345);
        Assertions.assertEquals(output, expected);
    }
}