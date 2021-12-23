package com.yikliu.leetcode.problems;

import java.util.Comparator;
import java.util.PriorityQueue;

import com.yikliu.leetcode.problems.datastructure.ListNode;

/**
 * You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
 *
 * Merge all the linked-lists into one sorted linked-list and return it.
 *
 *
 *
 * Example 1:
 *
 * Input: lists = [[1,4,5],[1,3,4],[2,6]]
 * Output: [1,1,2,3,4,4,5,6]
 * Explanation: The linked-lists are:
 * [
 *   1->4->5,
 *   1->3->4,
 *   2->6
 * ]
 * merging them into one sorted list:
 * 1->1->2->3->4->4->5->6
 *
 * Example 2:
 *
 * Input: lists = []
 * Output: []
 *
 * Example 3:
 *
 * Input: lists = [[]]
 * Output: []
 */
public class MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });
        ListNode cur;

        for (ListNode n : lists) {
            pq.offer(n);
        }

        ListNode dummy = new ListNode();
        cur = dummy;
        while(!pq.isEmpty()) {
            ListNode t = pq.poll();
            cur.next = t;
            if (t.next != null) {
                pq.offer(t.next);
            }
            cur = t;
        }
        return dummy.next;
    }
}
