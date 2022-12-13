# Leetcode Daily Challenge 12/7/2022
# 70. Climbing Stairs - EASY - Beats 96%
class Solution:
    def climbStairs(self, n: int) -> int:
        d1 = 1
        d2 = 1

        for _ in range(n - 1):
            oldD2 = d2
            d2 = d1 + d2
            d1 = oldD2

        return d2