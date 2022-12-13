# Leetcode Daily Challenge 12/7/2022
# 931. Minimum Falling Path Sum - MEDIUM - Beats 80%
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for y in range(len(matrix) - 2, -1, -1):
            for x in range(len(matrix[0])):
                matrix[y][x] += min(self.neighbors([y, x], matrix))

        return min(matrix[0])    
    
    
    def neighbors(self, coords, matrix):
        y, x = coords[0], coords[1]
        directions = [(1, -1), (1, 0), (1, 1)]
        l = []
        
        for dire in directions:
            dy, dx = dire[0], dire[1]
            if ( (x + dx >= len(matrix[0]))    or
                    (x + dx < 0)               or
                    (y + dy >= len(matrix))    or
                    (y + dy < 0) ):
                continue
            else:
                l.append(matrix[y + dy][x + dx])
                
        return l