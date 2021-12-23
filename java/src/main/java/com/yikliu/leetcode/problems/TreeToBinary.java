package com.yikliu.leetcode.problems;

import com.yikliu.leetcode.problems.datastructure.TreeNode;

/**
 * We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
 *
 * The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.
 *
 * Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.
 *
 * The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
 */
public class TreeToBinary {
    public TreeNode treeToDoublyList(TreeNode root) {
        if (root == null) return null;
        TreeNode head = null;
        TreeNode pre = null;
        inOrder(root, pre, head);
        head.left = pre;
        pre.right = head;
        return head;
    }

    private void inOrder(TreeNode cur, TreeNode pre, TreeNode head) {
        if (cur == null) return;
        inOrder(cur.left, pre, head);
        if (head == null) {
            head = cur;
            pre = cur;
        } else {
            pre.right = cur;
            cur.left = pre;
            pre = cur;
        }
        inOrder(cur.right, pre, head);
    }
}


