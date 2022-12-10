# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# I'M A FAILURE ... DIDN'T UNDERSTAND THIS ... RETURN TO THIS AGAIN
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = total = float("-inf")

        def mySum(node):
            if not node: return 0
            left, right = mySum(node.left), mySum(node.right)

            self.res = max(self.res, left * (total - left), (total - right) * right)
            return left + right + node.val

        total = mySum(root)
        mySum(root)
        return self.res % (10**9 + 7)
