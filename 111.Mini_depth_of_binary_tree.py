# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.left:
            return 1

        Q1 = [root]
        Q2 = []
        level = 1

        while Q1:
            for i in Q1:
                if not i.val:
                    continue
                if not i.left and not i.right:
                    return level
                elif not i.left and i.right:
                    Q2.append(i.right)
                elif i.left and not i.right:
                    Q2.append(i.left)
                else:
                    Q2.append(i.left)
                    Q2.append(i.right)
            level += 1
            Q1 = Q2
            Q2 = []
