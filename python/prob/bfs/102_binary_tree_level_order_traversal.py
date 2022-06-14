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
import TreeNode

from  collections imports deque

class BinaryTreeLevelOrderTraversal(unittest.TestCase):

    def levelOrder(root: TreeNode):
        result = []
        if not root:
            return [[]]

        q = deque()

        q.append(root)

        while q:
            level = []
            curSize = len(q)
            for i in range(curSize):
                node = q.popLeft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if q[i].right:
                    q.append(node.right)
            result.append(level)
        return result
