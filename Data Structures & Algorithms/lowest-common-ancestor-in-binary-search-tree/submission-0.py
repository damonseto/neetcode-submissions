# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            self.lower = p
            self.higher = q
        else:
            self.lower = q
            self.higher = p
        self.finalval = None
        def search(curr):
            if not curr:
                return
            if curr.val == self.lower.val or curr.val == self.higher.val:
                self.finalval = curr
                return
            if curr.val > self.lower.val and curr.val < self.higher.val:
                self.finalval = curr
                return
            if curr.val > self.higher.val:
                search(curr.left)
            else:
                search(curr.right)
        search(root)
        return self.finalval
        