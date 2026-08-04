# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.a = False
            
        def sametree(t1, t2):
            if not t1 and t2:
                return False
            if t1 and not t2:
                return False
            if not t1 and not t2:
                return True
            if t1.val != t2.val:
                return False
            return sametree(t1.left, t2.left) and sametree(t1.right, t2.right)
        
        def dfs(curr):
            if not curr:
                return
            if sametree(curr, subRoot):
                self.a = True
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return self.a
            