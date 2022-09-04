'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

import unittest
from collections import deque

from python.lib import TreeNode

class BinaryTreeLevelOrderTraversal(unittest.TestCase):

    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return [[]]

        q = deque()

        q.append(root)

        while q:
            level = []
            cur_size = len(q)
            for i in range(cur_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if q[i].right:
                    q.append(node.right)
            result.append(level)
        return result
