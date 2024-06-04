from python.lib import TreeNode
from collections import deque

def binary_tree_level_order_traverse(root: TreeNode):
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
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


