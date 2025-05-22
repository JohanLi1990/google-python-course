from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                
        for i in range(1, M):
            if matrix[i][0] == 0:
                self.flood_row(matrix, i, 1)
        for j in range(1, N):
            if matrix[0][j] == 0:
                self.flood_col(matrix, j, 1)
        if zero_col:
            self.flood_col(matrix, 0, 0)
        if zero_row:
            self.flood_row(matrix, 0, 0)
        
    def flood_row(self, matrix: List[List[int]], row: int, s:int):
        N = len(matrix[0])
        for j in range(s, N):
            matrix[row][j] = 0
    
    def flood_col(self, matrix: List[List[int]], col: int, s:int):
        M = len(matrix)
        for i in range(s, M):
            matrix[i][col] = 0
            

soln = Solution()
arr = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
soln.setZeroes(arr)
print(arr)
        