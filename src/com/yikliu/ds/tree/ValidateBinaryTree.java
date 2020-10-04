package com.yikliu.ds.tree;

public class ValidateBinaryTree {

    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }

    public boolean helper(TreeNode root, Integer lower,  Integer upper) {
        if (root == null) {
            return true;
        }

        if (lower != null && lower > root.val) return false;
        if (upper != null && upper < root.val) return false;

        return helper(root.left, lower, root.val) && helper(root.right, root.val, upper);
    }
}
