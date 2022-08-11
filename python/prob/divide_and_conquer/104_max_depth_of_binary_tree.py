'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

from python.lib import TreeNode

class MaxDepthOfBinaryTree:

    def recursive(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        if left >= right:
            return left + 1
        return right + 1

    def solution(self, root: TreeNode):
        return self.recursive(root)

