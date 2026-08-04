# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        if not root:
            return ans

        def bst(curr, l, r):
            if not curr:
                return
            if curr.val <= l or curr.val >= r:
                self.ans = False
                return
            bst(curr.left, l, curr.val)
            bst(curr.right, curr.val, r)
        bst(root, -1001, 1001)
        return self.ans

         