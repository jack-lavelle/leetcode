# Leetcode Daily Challenge 12/7/2022
# 938. Range Sum of BST - EASY - Beats 94%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.recursiveHelper(root, low, high)
    
    def recursiveHelper(self, node, low, high):
        leftsum = 0
        rightsum = 0
        if node.val > low:
            if node.left:
                leftsum += self.recursiveHelper(node.left, low, high)

        if node.val < high:
            if node.right:
                rightsum += self.recursiveHelper(node.right, low, high)
            
        totalsum = leftsum + rightsum
        
        if low <= node.val <= high:
            totalsum += node.val

        return totalsum
