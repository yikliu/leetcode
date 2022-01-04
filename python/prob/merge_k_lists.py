import unittest
import sys


class LinkNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def merge_k_lists(lists):
    count = {}
    max_value = -9999999
    min_value = 9999999
    for head in lists:
        cur = head
        while not cur:
            if cur.val > max_value:
                max_value = cur.val
            if cur.val < min_value:
                min_value = cur.val
            if cur.val in count:
                count[cur.val] += 1
            else:
                count[cur.val] = 1

    head = LinkNode()
    current = head

    for i in range(min, max):
        if i in count:
            for v in range(0, count[i]):
                n = LinkNode(i)
                current.next = n
                current = current.next

    return head.next
