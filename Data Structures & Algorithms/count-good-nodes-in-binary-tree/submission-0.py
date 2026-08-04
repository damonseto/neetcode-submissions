# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return 0
        def dfs(curr, max):
            if not curr:
                return
            new = max
            if curr.val >= max:
                self.count += 1
                new = curr.val
            dfs(curr.left, new)
            dfs(curr.right, new)
        dfs(root, 0)
        return self.count
            
            

