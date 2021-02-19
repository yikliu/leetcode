package com.yikliu.leetcode.problems;

import java.util.List;
import java.util.Stack;

public class LongestRectangleInHistogram {

    public int solve(List<Integer> heights) {
        Stack<Integer> stack = new Stack<>();
        int top = 0;
        int result = Integer.MIN_VALUE;
        heights.add(0);
        for (int i = 0; i < heights.size(); ) {
            if (stack.isEmpty() || heights.get(i) > heights.get(stack.peek())) {
                stack.push(i++);
            } else {
                top = stack.pop();
                result = Math.max(result, heights.get(top) * (stack.isEmpty() ? i : i - stack.peek() - 1));
            }
        }
        return result;
    }

}
