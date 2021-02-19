package com.yikliu.leetcode.problems;

import com.yikliu.leetcode.problems.datastructure.TreeNode;

public class SerializeTree {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        final StringBuilder sb = new StringBuilder();
        if (root != null) {
            helper(root, sb);
        }
        sb.append("#");
        return sb.toString();
    }

    private void helper(TreeNode root, StringBuilder sb) {
        sb.append(root.val).append(" ");
        if (root.left != null) {
            helper(root.left, sb);
        }
        if (root.right != null) {
            helper(root.right, sb);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] chunks = data.split(" ");
        return deserialize_helper(chunks, 0);
    }

    private TreeNode deserialize_helper(String[] chunks, int i) {
       if (i >= chunks.length || chunks[i].equals("#")) {
           return null;
       } else {
           TreeNode n = new TreeNode(Integer.parseInt(chunks[i]));
           i++;
           n.left = deserialize_helper(chunks, i);
           i++;
           n.right = deserialize_helper(chunks, i);
           return n;
       }
    }
}
