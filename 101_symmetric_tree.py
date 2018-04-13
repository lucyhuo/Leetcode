# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False


    def isSymmetric2(self, root):
        if not root:
            return True

        q = collections.deque([root.left,root.right])

        while q:
            left,right = q.popleft(), q.popleft()
            if not left and not right:
                continue
            if (not left or not right):
                return False
            if left.val != right.val:
                return False
            q += [left.left, right.right, left.right, right.left]

        return True





s = Solution()
s.isSymmetric()
