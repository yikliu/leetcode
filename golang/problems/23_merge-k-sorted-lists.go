package leetcode

/*
 * @lc app=leetcode id=23 lang=golang
 *
 * [23] Merge k Sorted Lists
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeKLists(lists []*ListNode) *ListNode {
	count := make(map[int]int)
	max, min := -1<<31, 1<<31-1
	for _, list := range lists {
		cur := list
		for cur != nil {
			if cur.Val > max {
				max = cur.Val
			}
			if cur.Val < min {
				min = cur.Val
			}
			count[cur.Val]++
			cur = cur.Next
		}
	}

	head := new(ListNode)
	cur := head

	for i := min; i <= max; i++ {
		c, present := count[i]
		if !present {
			continue
		}
		for j := 0; j < c; j++ {
			node := &ListNode{i, nil}
			cur.Next = node
			cur = cur.Next
		}
	}
	return head.Next
}
