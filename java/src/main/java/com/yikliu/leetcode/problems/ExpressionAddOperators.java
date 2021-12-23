package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a string that contains only digits 0-9 and a target value, return all possibilities to add binaryoperators (not unary) +, -, or * between the digits so they evaluate to the target value.
 *
 * Example 1:
 *
 * Input: _num_ = "123", _target_ = 6
 * Output: ["1+2+3", "1*2*3"]
 * Example 2:
 *
 * Input: _num_ = "232", _target_ = 8
 * Output: ["2*3+2", "2+3*2"]
 * Example 3:
 *
 * Input: _num_ = "105", _target_ = 5
 * Output: ["1*0+5","10-5"]
 * Example 4:
 *
 * Input: _num_ = "00", _target_ = 0
 * Output: ["0+0", "0-0", "0*0"]
 * Example 5:
 *
 * Input: _num_ = "3456237490", _target_ = 9191
 * Output: []
 */
public class ExpressionAddOperators {
    public List<String> addOperators(String num, int target) {
        List<String> ans = new ArrayList<>();
        helper(target, 0, num, "", ans);
        return ans;
    }

    private void helper(int target, int curValue, String curNum, String curExpression, List<String> res) {
        if (curNum.length() == 0 && curValue == target) {
            res.add(curExpression);
            return;
        }
        for (int i = 0; i < curNum.length(); i++) {
            String next = curNum.substring(i);
            String num = curNum.substring(0, i);
            if (curExpression.length() > 0) {
                helper(target, curValue + Integer.parseInt(num), next, curExpression + " + " + num, res);
                helper(target, curValue - Integer.parseInt(num), next, curExpression + " - " + num, res);
            } else {
                helper(target, curValue, next, curExpression, res);
            }
        }
    }
}
