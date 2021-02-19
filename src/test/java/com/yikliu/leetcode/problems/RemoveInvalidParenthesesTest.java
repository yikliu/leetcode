package com.yikliu.leetcode.problems;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class RemoveInvalidParenthesesTest {
    private RemoveInvalidParentheses mRemoveInvalidParentheses;

    @BeforeEach
    public void setup() {
        mRemoveInvalidParentheses = new RemoveInvalidParentheses();
    }

    @Test
    public void test() {
        final List<String> expected = Arrays.asList("(a)()()", "(a())()");
        final String input = "(a)())()";
        final List<String> output = mRemoveInvalidParentheses.solve(input);
        Assertions.assertEquals(expected.size(), output.size());
        Assertions.assertTrue(expected.containsAll(output));
        Assertions.assertTrue(output.containsAll(expected));
    }
}
