# Definition for a binary tree node.
# 1026. Maximum Difference Between Node and Ancestor - MEDIUM - Beats 94%
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recursiveHelper(root, float("-inf"), float("inf"))
    def recursiveHelper(self, node, maxi, mini):
        left = float("-inf")
        right = float("-inf")
        
        maxi = max(node.val, maxi)
        mini = min(node.val, mini)

        if node.left:
            left = self.recursiveHelper(node.left, maxi, mini)

        if node.right:
            right = self.recursiveHelper(node.right, maxi, mini)

        return max(left, right, abs(maxi - node.val), abs(mini - node.val))
