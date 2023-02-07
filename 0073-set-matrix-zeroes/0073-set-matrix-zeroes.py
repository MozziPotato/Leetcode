class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        height = len(matrix)
        width = len(matrix[0])
        col_zero_exist = False
        row_zero_exist = False
        
        for i in range(height):
            if matrix[i][0] == 0:
                col_zero_exist = True
        
        for j in range(width):
            if matrix[0][j] == 0:
                row_zero_exist = True
        
        for i in range(height):
            for j in range(width):
                value = matrix[i][j]
                if not value:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,height):
            if matrix[i][0] == 0:
                for j in range(width):
                    matrix[i][j] = 0
        
        for j in range(1,width):
            if matrix[0][j] == 0:
                for i in range(height):
                    matrix[i][j] = 0
        
        if col_zero_exist:
            for i in range(height):
                matrix[i][0] = 0
        
        if row_zero_exist:
            for j in range(width):
                matrix[0][j] = 0