
import collections
class Solution:
    def levelOrderBottom1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        self.BFS(root,0,res)
        return res
        
    def BFS(self, root, level, res):
        if not root:
            return
        if len(res) < level +1:
            res.insert(0,[])
        res[-(level+1)].append(root.val)
        self.BFS(root.left, level + 1, res)
        self.BFS(root.right, level + 1, res)
    
    def levelOrderBottom(self, root):
        q = collections.deque([(root,0)])
        res = []
        while q:
            root, level = q.popleft()
            if not root:
                continue
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            q.append((root.left,level+1))
            q.append((root.right,level+1))
            
        return res[::-1]