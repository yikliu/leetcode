package com.yikliu.leetcode.problems;

/**
 * Input: a = "11", b = "1"
 * Output: "100"
 */
public class AddBinary {
    public String addBinary(String a, String b) {
        int sa = a.length();
        String res = "";
        int sb = b.length();
        int p, q, sum = 0, carry = 0;
        for (int m = sa - 1, n = sb - 1; m >= 0 || n >=0; m--, n--) {
            p = a.charAt(m) - '0';
            q = b.charAt(n) - '0';
            sum = (p + q + carry) % 2;
            res = sum + res;
            carry = (p + q + carry) / 2;
        }
        return carry == 1 ? "1" + res : res;
    }
}
