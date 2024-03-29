package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

import com.yikliu.leetcode.problems.datastructure.TreeNode;

import javafx.util.Pair;

/**
 * Given a binary tree, return the  vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
 *
 * If two nodes are in the same row and column, the order should be from left to right.
 *
 * Examples 1:
 *
 * Input: [3,9,20,null,null,15,7]
 *
 *    3
 *   /\
 *  /  \
 *  9  20
 *     /\
 *    /  \
 *   15   7
 *
 * Output:
 *
 * [
 *   [9],
 *   [3,15],
 *   [20],
 *   [7]
 * ]
 *
 * Examples 2:
 *
 * Input: [3,9,8,4,0,1,7]
 *
 *      3
 *     /\
 *    /  \
 *    9   8
 *   /\  /\
 *  /  \/  \
 *  4  01   7
 *
 * Output:
 *
 * [
 *   [4],
 *   [9],
 *   [3,0,1],
 *   [8],
 *   [7]
 * ]
 *
 * Examples 3:
 *
 * Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
 *
 *      3
 *     /\
 *    /  \
 *    9   8
 *   /\  /\
 *  /  \/  \
 *  4  01   7
 *     /\
 *    /  \
 *    5   2
 *
 * Output:
 *
 * [
 *   [4],
 *   [9,5],
 *   [3,0,1],
 *   [8,2],
 *   [7]
 * ]
 */
public class BinaryTreeVerticalTraverse {
    List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        TreeMap<Integer, List<Integer>> map = new TreeMap<>();
        Queue<Pair<Integer, TreeNode>> q = new LinkedList<>();
        q.offer(new Pair<>(0, root));
        while (!q.isEmpty()) {
            Pair<Integer, TreeNode> head = q.poll();
            if (map.containsKey(head.getKey())) {
                map.get(head.getKey()).add(head.getValue().val);
            } else {
                map.put(head.getKey(), Arrays.asList(head.getValue().val));
            }
            if (head.getValue().left != null) {
                q.offer(new Pair<>(head.getKey() - 1, head.getValue().left));
            }
            if (head.getValue().right != null) {
                q.offer(new Pair<>(head.getKey() + 1, head.getValue().right));
            }
        }
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            res.add(entry.getValue());
        }
        return res;
    }
}


