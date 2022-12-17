'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

'''

from typing import Optional, Union
from python.lib import TreeNode


def getDirections(root: Optional[TreeNode], start_value: int, dest_value: int) -> str:
    # find the path from root to source and dest
    found, path_s = getPath(root, start_value)
    found, path_d = getPath(root, dest_value)

    # i is the count of identical nodes in the path of root->start and root->desk
    i = 0
    while i < len(path_s) and i < len(path_d) and path_s[i] == path_d[i]:
        i += 1

    # replace the identical nodes with "U"
    ans = ""
    for j in range(len(path_s) - i):
        ans += "U"
    return ans + path_d[i:]


def getPath(root: Optional[TreeNode], val: int) -> Union[bool, str]:
    if not root:
        return False, ""
    if root.val == val:
        return True, ""

    found, path = getPath(root.left, val)

    if found:
        return True, "L" + path
    else:
        found, path = getPath(root.right, val)

        if found:
            return True, "R" + path
        else:
            return False, ""
