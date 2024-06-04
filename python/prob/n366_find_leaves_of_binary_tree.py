'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example: Given binary tree

          1
         / \
        2   3
       / \     
      4   5
Returns [4, 5, 3], [2], [1].
'''

from python.lib.tree_node import TreeNode
from typing import List


def find_leaves_in_binary_tree(root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root:
                return -1
            depth = max(dfs(root.left), dfs(root.right)) + 1
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            return depth
        res = []
        dfs(root)
        return res