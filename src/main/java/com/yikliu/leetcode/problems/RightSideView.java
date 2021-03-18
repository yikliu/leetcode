package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import com.yikliu.leetcode.problems.datastructure.TreeNode;

/*
Given a binary tree, imagine yourself standing on the  right  side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---



You should return [1, 3, 4].
 */
public class RightSideView {
    /**
     * Can't just iterate on right child, because if left depth is larger than right. still want to see the one on left side
     */
    public List<Integer> rightSideView(TreeNode root) {
        LinkedList<TreeNode> level = new LinkedList<>();
        level.offer(root);
        List<Integer> res = new ArrayList<>();
        while(!level.isEmpty()) { //each iteration of while is executing one level of nodes.
            res.add(level.getLast().val);
            for (int i = 0; i < level.size(); i++) {
                TreeNode head = level.poll();
                if (head != null) {
                    if (head.left != null) {
                        level.offer(head.left);
                    }
                    if (head.right != null) {
                        level.offer(head.right);
                    }
                }
            }
        }
        return res;
    }
}
