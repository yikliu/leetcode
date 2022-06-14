'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
'''
import TreeNode

class LevelOrderII:

    def solution(root: TreeNode)->List[List[int]]:
        if not root: 
            return []
        q = deque()
        s = deque()

        q.append(root)

        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popLeft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            s.append(level)
        result = []
        while s:
            result.append(s.pop())
        return result

