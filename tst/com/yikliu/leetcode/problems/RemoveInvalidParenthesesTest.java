package com.yikliu.leetcode.problems;

import java.util.Arrays;
import java.util.List;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class RemoveInvalidParenthesesTest {
    private RemoveInvalidParentheses mRemoveInvalidParentheses;

    @BeforeClass
    public void setup() {
        mRemoveInvalidParentheses = new RemoveInvalidParentheses();
    }

    @Test
    public void test() {
        final List<String> expected = Arrays.asList("(a)()()", "(a())()");
        final String input = "(a)())()";
        final List<String> output = mRemoveInvalidParentheses.solve(input);
        Assert.assertEquals(expected.size(), output.size());
        Assert.assertTrue(expected.containsAll(output));
        Assert.assertTrue(output.containsAll(expected));
    }
}
