# pylint: skip-file

from collections import deque


def binary_tree_vertical_traverse(root):
    if not root:
        return [] 
    map = {}
    q = deque([0, root])
    ans = []
    while q.size > 0: 
        head = q.popLeft(0)
        map.setdefault(head[0], []).append(head[1].val)
        if not head[1].left:
            q.append([head[0]-1, head[1].left])
        if not head[1].right:
            q.append([head[0]-1, head[1].right])
        for k, v in sorted(map).items():
            ans.append(v)
    return ans
