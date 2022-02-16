package com.yikliu.leetcode.problems;

import com.yikliu.leetcode.problems.datastructure.TreeNode;

public class MaxSumPathBinaryTree {

    public int maxSumPath(TreeNode root) {
        WrapInt res = new WrapInt();
        res.value = 0;
        helper(root, res);
        return res.value;
    }

    public int helper(TreeNode node, WrapInt res) {
        if (node == null) return res.value;
        int left = Math.max(helper(node.left, res), 0);
        int right = Math.max(helper(node.right, res), 0);
        res.value = Math.max(res.value, left + right + node.val);
        return Math.max(left, right) + node.val;
    }
}

/**
 * Because pass by reference.
 */
class WrapInt{
    int value;
}
